from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, User, FormSubmission
from datetime import datetime
import os

# Initialize Flask app
app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bussutech.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_SORT_KEYS'] = False

# Initialize database
db.init_app(app)

# Enable CORS for all routes (allows frontend to make requests)
CORS(app, resources={
    r"/api/*": {
        "origins": ["http://localhost", "http://localhost:5000", "http://127.0.0.1:5000", "file://"],
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type"]
    }
})

# Create database tables
with app.app_context():
    db.create_all()


# ============================================================================
# HEALTH CHECK
# ============================================================================

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'ok', 'message': 'BussuTech API is running'}), 200


# ============================================================================
# USER REGISTRATION
# ============================================================================

@app.route('/api/auth/signup', methods=['POST'])
def signup():
    """Register a new user"""
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['first_name', 'last_name', 'email', 'password', 'password_confirm']
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Missing required fields'}), 400
        
        # Validate passwords match
        if data['password'] != data['password_confirm']:
            return jsonify({'error': 'Passwords do not match'}), 400
        
        # Validate password strength (8+ chars, uppercase, lowercase, number)
        password = data['password']
        if len(password) < 8:
            return jsonify({'error': 'Password must be at least 8 characters'}), 400
        if not any(c.isupper() for c in password):
            return jsonify({'error': 'Password must contain uppercase letter'}), 400
        if not any(c.islower() for c in password):
            return jsonify({'error': 'Password must contain lowercase letter'}), 400
        if not any(c.isdigit() for c in password):
            return jsonify({'error': 'Password must contain a number'}), 400
        
        # Check if user exists
        existing_user = User.query.filter_by(email=data['email']).first()
        if existing_user:
            return jsonify({'error': 'Email already registered'}), 409
        
        # Create new user
        user = User(
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'],
            newsletter_subscribed=data.get('newsletter', False)
        )
        user.set_password(data['password'])
        
        db.session.add(user)
        db.session.commit()
        
        return jsonify({
            'message': 'Account created successfully',
            'user': user.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


# ============================================================================
# USER LOGIN
# ============================================================================

@app.route('/api/auth/login', methods=['POST'])
def login():
    """Authenticate user and return user data"""
    try:
        data = request.get_json()
        
        # Validate required fields
        if not data.get('email') or not data.get('password'):
            return jsonify({'error': 'Email and password required'}), 400
        
        # Find user by email
        user = User.query.filter_by(email=data['email']).first()
        
        if not user or not user.check_password(data['password']):
            return jsonify({'error': 'Invalid email or password'}), 401
        
        return jsonify({
            'message': 'Login successful',
            'user': user.to_dict()
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# ============================================================================
# GET USER PROFILE
# ============================================================================

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Get user profile by ID"""
    try:
        user = User.query.get(user_id)
        
        if not user:
            return jsonify({'error': 'User not found'}), 404
        
        return jsonify(user.to_dict()), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# ============================================================================
# CONTACT FORM SUBMISSION
# ============================================================================

@app.route('/api/contact/submit', methods=['POST'])
def submit_contact_form():
    """Store contact form submission"""
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['name', 'email', 'subject', 'category', 'message']
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Missing required fields'}), 400
        
        # Create form submission
        submission = FormSubmission(
            name=data['name'],
            email=data['email'],
            subject=data['subject'],
            category=data['category'],
            message=data['message'],
            user_id=data.get('user_id')  # Optional if user is logged in
        )
        
        db.session.add(submission)
        db.session.commit()
        
        return jsonify({
            'message': 'Form submitted successfully',
            'submission': submission.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


# ============================================================================
# GET FORM SUBMISSIONS (Admin view)
# ============================================================================

@app.route('/api/contact/submissions', methods=['GET'])
def get_submissions():
    """Get all form submissions (admin endpoint)"""
    try:
        submissions = FormSubmission.query.order_by(FormSubmission.created_at.desc()).all()
        
        return jsonify({
            'total': len(submissions),
            'submissions': [sub.to_dict() for sub in submissions]
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# ============================================================================
# UPDATE FORM SUBMISSION STATUS
# ============================================================================

@app.route('/api/contact/submissions/<int:submission_id>', methods=['PUT'])
def update_submission_status(submission_id):
    """Update form submission status"""
    try:
        submission = FormSubmission.query.get(submission_id)
        
        if not submission:
            return jsonify({'error': 'Submission not found'}), 404
        
        data = request.get_json()
        
        if 'status' in data:
            submission.status = data['status']
            submission.updated_at = datetime.utcnow()
            db.session.commit()
        
        return jsonify({
            'message': 'Submission updated',
            'submission': submission.to_dict()
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


# ============================================================================
# GET ALL USERS (Admin view)
# ============================================================================

@app.route('/api/users', methods=['GET'])
def get_all_users():
    """Get all users (admin endpoint)"""
    try:
        users = User.query.all()
        
        return jsonify({
            'total': len(users),
            'users': [user.to_dict() for user in users]
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# ============================================================================
# ERROR HANDLERS
# ============================================================================

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({'error': 'Endpoint not found'}), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    db.session.rollback()
    return jsonify({'error': 'Internal server error'}), 500


if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True, port=5000, host='127.0.0.1')
