# HTML_CSS_JavaScript Project

A comprehensive web project showcasing HTML, CSS, and JavaScript fundamentals with modern best practices for accessibility, responsive design, and code organization.

## 📁 Project Structure

```
HTML_CSS_JavaScript/
├── css/
│   ├── global.css          # Shared styles and design system
│   ├── login.css           # Login page specific styles
│   └── index.css           # Home page specific styles
├── Media/                  # Images and media files
│   ├── Favicon.png
│   ├── DevHub-logo.png
│   └── Good Morning.mp4
├── index.html              # Home page
├── login.html              # Login/Signup page
├── Mywebsite.html          # Clean login form template
├── CounterProgram.html     # Interactive counter app
├── CounterProgram.css      # Counter app styles
├── CounterProgram.js       # Counter app logic
├── submit_form.php         # Form submission handler (backend)
└── README.md               # This file
```

## 🎯 Features

### 1. **Global Design System**
   - CSS custom properties (variables) for consistent colors, spacing, and typography
   - Unified color palette and font stack across all pages
   - Responsive breakpoints for mobile, tablet, and desktop
   - Utility classes for common styling patterns

### 2. **Home Page (index.html)**
   - Professional landing page with company information
   - Interactive product table with semantic HTML
   - Embedded video player
   - Professional header and footer

### 3. **Login/Signup Page (login.html)**
   - Clean, accessible login form
   - Form validation with HTML5 attributes
   - Password requirements indicator
   - Responsive design for all devices

### 4. **Counter Application**
   - Interactive counter with increase, decrease, and reset buttons
   - Real-time value display
   - Modern gradient UI with smooth animations
   - ARIA labels for screen reader compatibility

### 5. **Accessibility Features**
   - Semantic HTML5 elements (`<header>`, `<main>`, `<section>`, `<nav>`, `<footer>`)
   - ARIA labels and roles for screen readers
   - Keyboard navigation support
   - Color contrast compliance
   - Skip navigation links (screen reader only)

### 6. **Responsive Design**
   - Mobile-first approach
   - Breakpoints for tablets (768px) and phones (480px)
   - Flexible layouts with flexbox
   - Optimized touch targets for mobile devices

## 🚀 Getting Started

### Prerequisites
- A modern web browser (Chrome, Firefox, Safari, Edge)
- Optional: Local web server for testing PHP forms

### Setup

1. **Clone or download the project**
   ```bash
   git clone <repository-url>
   cd HTML_CSS_JavaScript
   ```

2. **Open in browser**
   - Double-click `index.html` to open the home page
   - Or use a local web server:
     ```bash
     python -m http.server 8000
     # Visit http://localhost:8000
     ```

3. **For PHP form handling**
   - Use a local PHP server:
     ```bash
     php -S localhost:8000
     ```
   - Or deploy to a web server with PHP support

## 📖 Pages Overview

### Home Page (`index.html`)
- Navigation menu with links to all pages
- Company introduction and information
- Product showcase table
- Embedded video player
- Call-to-action buttons

**Access:** Open `index.html` in your browser

### Login Page (`login.html`)
- Username and email input fields
- Secure password input with validation
- Form submission to backend
- Link to signup page
- Consistent branding with home page

**Access:** From home page, click "Login" or open `login.html` directly

### Counter App (`CounterProgram.html`)
- Large, easy-to-read counter display
- Three action buttons: Decrease, Reset, Increase
- Real-time value updates
- Beautiful gradient background
- Fully responsive design

**Access:** Open `CounterProgram.html` in your browser

### Clean Login Template (`Mywebsite.html`)
- Minimal, professional login form
- Centered design with modern styling
- Ready to customize for other projects

## 🎨 Customization

### Changing Colors
Edit the CSS custom properties in `css/global.css`:

```css
:root {
    --color-primary: #007BFF;        /* Change primary color */
    --color-primary-dark: #0056b3;   /* Change dark variant */
    --color-danger: #dc4c46;         /* Change danger color */
}
```

### Modifying Typography
Update font settings in `css/global.css`:

```css
:root {
    --font-family-base: 'Segoe UI', Arial, sans-serif;  /* Change font */
    --font-size-base: 16px;                              /* Change base size */
}
```

### Adding New Pages
1. Create a new HTML file in the root directory
2. Include the global CSS:
   ```html
   <link rel="stylesheet" href="css/global.css">
   ```
3. Create a page-specific CSS file in the `css/` folder if needed
4. Add navigation links to existing pages

## 🔄 JavaScript Features

### Counter Application (`CounterProgram.js`)
```javascript
// Event listeners for counter buttons
- decreaseButton.onclick → Decrements counter
- increaseButton.onclick → Increments counter
- resetButton.onclick → Resets to zero
```

Features:
- Simple, readable code
- No external dependencies
- Real-time DOM updates
- Event-driven architecture

## 🌐 Browser Compatibility

| Browser | Support |
|---------|---------|
| Chrome  | ✅ Full |
| Firefox | ✅ Full |
| Safari  | ✅ Full |
| Edge    | ✅ Full |
| IE 11   | ⚠️ Partial |

## 📱 Responsive Breakpoints

- **Desktop:** 1200px+ (full layout)
- **Tablet:** 768px - 1199px (adjusted spacing, single column tables)
- **Mobile:** Below 768px (optimized for small screens)
- **Small Mobile:** Below 480px (minimal padding, larger touch targets)

## ♿ Accessibility Checklist

- ✅ Semantic HTML5 elements
- ✅ ARIA labels and descriptions
- ✅ Keyboard navigation support
- ✅ Color contrast (WCAG AA standard)
- ✅ Focus indicators on interactive elements
- ✅ Screen reader compatibility
- ✅ Form labels properly associated with inputs
- ✅ Alternative text for images

## 🔒 Security Notes

### For Production:
1. **Form Handling**
   - Validate all user inputs server-side
   - Use prepared statements to prevent SQL injection
   - Implement CSRF tokens

2. **Password Security**
   - Never store passwords in plain text
   - Use secure hashing algorithms (bcrypt, Argon2)
   - Implement password reset functionality

3. **HTTPS**
   - Always use HTTPS in production
   - Update external links to HTTPS

## 📝 Best Practices Implemented

1. **CSS Organization**
   - Global styles separated from page-specific styles
   - CSS custom properties for maintainability
   - Mobile-first responsive design

2. **HTML Structure**
   - Semantic HTML5 elements for better SEO and accessibility
   - Proper heading hierarchy
   - Logical DOM structure

3. **JavaScript**
   - Event-driven architecture
   - Clear variable naming
   - No global scope pollution

4. **Performance**
   - Minimal HTTP requests
   - Optimized CSS (no unused styles)
   - Fast JavaScript execution

## 🐛 Known Issues & Future Improvements

### Current Limitations:
- `About_us.html`, `Contact_us.html`, and `SignUp.html` referenced but not included
- PHP backend not fully implemented
- No database integration

### Planned Enhancements:
- [ ] Add missing pages (About, Contact, Signup)
- [ ] Implement PHP backend for form submission
- [ ] Add form validation with JavaScript
- [ ] Create a database schema for user management
- [ ] Add user authentication system
- [ ] Implement dark mode toggle
- [ ] Add loading indicators
- [ ] Create admin dashboard

## 📧 Contact & Support

For issues or questions:
- **Author:** Vamshi
- **Email:** [Your Email]
- **Website:** [Your Website]

## 📄 License

This project is provided for educational and practice purposes. Feel free to use, modify, and share for learning.

---

**Last Updated:** May 2026

**Project Version:** 2.0 (Refactored with modern best practices)
