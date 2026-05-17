# Quick Start Guide - BussuTech Backend

## 🚀 Get Started in 3 Minutes

### Step 1: Install Dependencies

```bash
cd backend
pip install -r requirements.txt
```

**What this does:**
- Installs Flask web framework
- Installs SQLAlchemy for database ORM
- Installs CORS for cross-origin requests
- Installs python-dotenv for environment variables

### Step 2: Initialize Database

```bash
python init_db.py
```

**What this does:**
- Creates SQLite database file: `bussutech.db`
- Creates tables for users and form submissions
- Adds sample users for testing

**Sample Test Users:**
```
Email: vamshi@bussutech.com
Password: BussuTech123

Email: demo@bussutech.com  
Password: DemoUser123
```

### Step 3: Start the Server

```bash
python app.py
```

**Expected Output:**
```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

🎉 Your API is now running!

---

## 🧪 Test the API

### Using your browser:

Visit: `http://127.0.0.1:5000/api/health`

You should see:
```json
{
  "status": "ok",
  "message": "BussuTech API is running"
}
```

### Using curl (command line):

**Test signup:**
```bash
curl -X POST http://127.0.0.1:5000/api/auth/signup \
  -H "Content-Type: application/json" \
  -d '{
    "first_name": "John",
    "last_name": "Doe",
    "email": "john@example.com",
    "password": "MyPassword123",
    "password_confirm": "MyPassword123"
  }'
```

**Test login:**
```bash
curl -X POST http://127.0.0.1:5000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "vamshi@bussutech.com",
    "password": "BussuTech123"
  }'
```

**Submit contact form:**
```bash
curl -X POST http://127.0.0.1:5000/api/contact/submit \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "email": "john@example.com",
    "subject": "Hello",
    "category": "support",
    "message": "I have a question",
    "user_id": 1
  }'
```

---

## 📱 Testing Frontend Forms

The HTML pages are already configured to use the API!

### Test Login Page:
1. Go to `login.html`
2. Use test credentials above
3. Check browser console for API response

### Test Signup Page:
1. Go to `signup.html`
2. Fill form with new email and password (8+ chars, uppercase, lowercase, number)
3. Form data will be sent to database

### Test Contact Form:
1. Go to `contact.html`
2. Fill in all fields
3. Click "Send Message"
4. Data will be saved to database

---

## 📊 Database Files

- **SQLite Database**: `backend/instance/bussutech.db`
- **Models**: `backend/models.py`
- **API Code**: `backend/app.py`

### View Database Content (Python):

```python
from app import app
from models import User, FormSubmission

with app.app_context():
    users = User.query.all()
    for user in users:
        print(f"{user.first_name} {user.last_name} - {user.email}")
    
    submissions = FormSubmission.query.all()
    for sub in submissions:
        print(f"From: {sub.name} - {sub.subject}")
```

---

## 🔒 Admin View

Get all users and submissions (useful for admin dashboard):

```bash
# Get all users
curl http://127.0.0.1:5000/api/users

# Get all form submissions  
curl http://127.0.0.1:5000/api/contact/submissions

# Update submission status
curl -X PUT http://127.0.0.1:5000/api/contact/submissions/1 \
  -H "Content-Type: application/json" \
  -d '{"status": "replied"}'
```

---

## 🛑 Troubleshooting

**Error: "Port 5000 already in use"**
- Another process is using port 5000
- Edit `app.py` and change: `app.run(debug=True, port=5001)`

**Error: "ModuleNotFoundError: No module named 'flask'"**
- Dependencies not installed
- Run: `pip install -r requirements.txt`

**Error: "Database locked"**
- Close all connections to database
- Delete `backend/instance/bussutech.db`
- Run: `python init_db.py`

**Forms not sending data to API**
- Check browser console (F12) for errors
- Verify API is running on `http://127.0.0.1:5000`
- Check that api-client.js is loaded before main.js

---

## 📝 Project Structure

```
HTML_CSS_JavaScript/
├── backend/
│   ├── app.py              # Flask application & API endpoints
│   ├── models.py           # Database models (User, FormSubmission)
│   ├── init_db.py          # Database initialization script
│   ├── requirements.txt     # Python dependencies
│   └── README.md           # Full API documentation
├── js/
│   ├── api-client.js       # API client library (NEW)
│   └── main.js             # Form handlers (UPDATED)
├── index.html
├── login.html
├── signup.html
├── contact.html
├── about.html
└── counter.html
```

---

## ✨ What's Working

✅ User registration with password hashing
✅ User login authentication  
✅ Contact form submissions
✅ Form validation on both frontend & backend
✅ Data stored in SQLite database
✅ Proper error messages and status codes
✅ Admin endpoints for viewing submissions
✅ Browser localStorage for logged-in user

---

## 🔜 Next Steps

1. **Customize** - Edit API endpoints in `backend/app.py`
2. **Deploy** - Host on Heroku, AWS, or your own server
3. **Extend** - Add more endpoints as needed
4. **Secure** - Add JWT authentication for production
5. **Monitor** - Set up logging and error tracking

---

## 📧 Support

Need help? Check the full README in `backend/README.md`

Happy coding! 🎉
