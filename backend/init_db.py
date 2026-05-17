"""
Initialize the BussuTech database with sample data
Run this file once to set up the database
"""

from app import app, db
from models import User, FormSubmission

def init_db():
    """Initialize the database"""
    with app.app_context():
        # Drop all existing tables (optional, for fresh start)
        # db.drop_all()
        
        # Create all tables
        db.create_all()
        
        # Check if sample data already exists
        if User.query.first() is None:
            print("Creating sample users...")
            
            # Create sample users
            user1 = User(
                first_name='Vamshi',
                last_name='Reddy',
                email='vamshi@bussutech.com',
                newsletter_subscribed=True
            )
            user1.set_password('BussuTech123')
            
            user2 = User(
                first_name='Demo',
                last_name='User',
                email='demo@bussutech.com',
                newsletter_subscribed=False
            )
            user2.set_password('DemoUser123')
            
            db.session.add(user1)
            db.session.add(user2)
            db.session.commit()
            
            print(f"✓ Created {User.query.count()} users")
        
        print(f"✓ Database initialized successfully!")
        print(f"  - Users: {User.query.count()}")
        print(f"  - Form Submissions: {FormSubmission.query.count()}")

if __name__ == '__main__':
    init_db()
