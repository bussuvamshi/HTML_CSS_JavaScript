# BussuTech Backend - Flask API

A Python/Flask backend for storing user login credentials and form submissions in SQLite database.

## Features

✅ **User Authentication**
- User registration with email validation
- User login with password verification
- Password hashing with Werkzeug security
- Newsletter subscription management

✅ **Data Storage**
- SQLite database for persistent data storage
- User profiles (name, email, newsletter preference)
- Contact form submissions with categories

✅ **RESTful API**
- 8 API endpoints for frontend integration
- CORS enabled for cross-origin requests
- JSON request/response format
- Proper error handling and status codes

✅ **Database Models**
- `User` model - stores user registration data
- `FormSubmission` model - stores contact form submissions

## Installation

### 1. Navigate to backend directory

```bash
cd backend
```

### 2. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 3. Initialize the database

```bash
python init_db.py
```

This creates the SQLite database with sample users:
- Email: `vamshi@bussutech.com` | Password: `BussuTech123`
- Email: `demo@bussutech.com` | Password: `DemoUser123`

## Running the Server

```bash
python app.py
```

The API will be available at: `http://127.0.0.1:5000`

## API Endpoints

### Health Check

**GET** `/api/health`
- Verify API is running
- No authentication required

### User Authentication

**POST** `/api/auth/signup`
- Register a new user
- Body: `{ first_name, last_name, email, password, password_confirm, newsletter }`
- Returns: `{ message, user }`

**POST** `/api/auth/login`
- Authenticate user credentials
- Body: `{ email, password }`
- Returns: `{ message, user }`

### User Management

**GET** `/api/users/<user_id>`
- Get user profile by ID
- Returns: User object

**GET** `/api/users`
- Get all users (admin)
- Returns: `{ total, users }`

### Contact Forms

**POST** `/api/contact/submit`
- Submit a contact form
- Body: `{ name, email, subject, category, message, user_id }`
- Returns: `{ message, submission }`

**GET** `/api/contact/submissions`
- Get all form submissions (admin)
- Returns: `{ total, submissions }`

**PUT** `/api/contact/submissions/<submission_id>`
- Update submission status
- Body: `{ status }`
- Returns: `{ message, submission }`

## Frontend Integration

The frontend uses `js/api-client.js` to interact with this API.

### Key Functions

```javascript
// Authentication
registerUser(userData)
loginUser(email, password)
getUserProfile(userId)

// Contact Forms
submitContactForm(formData)
getFormSubmissions()
updateSubmissionStatus(submissionId, status)

// Admin
getAllUsers()
checkAPIHealth()
```

### Example Usage in HTML

```html
<!-- Include the API client -->
<script src="js/api-client.js" defer></script>
<script src="js/main.js" defer></script>

<!-- In your form handler -->
<script>
async function handleSubmit(event) {
    event.preventDefault();
    try {
        const response = await submitContactForm({
            name: 'John Doe',
            email: 'john@example.com',
            subject: 'Hello',
            category: 'support',
            message: 'I have a question'
        });
        console.log('Submitted:', response.submission);
    } catch (error) {
        console.error('Error:', error);
    }
}
</script>
```

## Database Schema

### users table

| Column | Type | Notes |
|--------|------|-------|
| id | INTEGER | Primary key |
| first_name | VARCHAR(100) | User's first name |
| last_name | VARCHAR(100) | User's last name |
| email | VARCHAR(120) | Unique, indexed |
| password_hash | VARCHAR(255) | Hashed password |
| newsletter_subscribed | BOOLEAN | Newsletter preference |
| created_at | DATETIME | Account creation time |
| updated_at | DATETIME | Last update time |

### form_submissions table

| Column | Type | Notes |
|--------|------|-------|
| id | INTEGER | Primary key |
| user_id | INTEGER | Foreign key to users |
| name | VARCHAR(200) | Submitter's name |
| email | VARCHAR(120) | Submitter's email |
| subject | VARCHAR(255) | Form subject |
| category | VARCHAR(100) | Form category |
| message | TEXT | Form message |
| status | VARCHAR(50) | new/read/replied/resolved |
| created_at | DATETIME | Submission time |
| updated_at | DATETIME | Last update time |

## Password Requirements

Passwords must meet these criteria:
- Minimum 8 characters
- At least one uppercase letter (A-Z)
- At least one lowercase letter (a-z)
- At least one number (0-9)

## Error Handling

All endpoints return proper HTTP status codes:

- **200** - Success
- **201** - Created
- **400** - Bad Request (missing/invalid fields)
- **401** - Unauthorized (wrong credentials)
- **404** - Not Found
- **409** - Conflict (email already exists)
- **500** - Server Error

Error responses include a JSON body with error message:
```json
{ "error": "Email already registered" }
```

## Local Storage

When a user logs in, their data is stored in browser's localStorage:

```javascript
localStorage.setItem('currentUser', JSON.stringify(user));
```

Access it later:
```javascript
const user = JSON.parse(localStorage.getItem('currentUser'));
```

## Development Notes

- API runs in debug mode on `127.0.0.1:5000`
- Database file: `backend/instance/bussutech.db`
- All routes have CORS enabled for local development
- Passwords are securely hashed using Werkzeug's security module

## Future Enhancements

- [ ] Email verification for new accounts
- [ ] Password reset functionality
- [ ] JWT authentication tokens
- [ ] Rate limiting
- [ ] Admin dashboard
- [ ] Email notifications
- [ ] User profile updates
- [ ] Submission attachments

## Troubleshooting

**Issue:** "Address already in use" error
- Change port in `app.py`: `app.run(debug=True, port=5001)`

**Issue:** Database locked error
- Delete `backend/instance/bussutech.db` and run `init_db.py` again

**Issue:** CORS errors
- Ensure api-client.js is loaded before main.js
- Check API_BASE_URL in api-client.js matches your server URL

## Support

For issues or questions, please contact: support@bussutech.com
