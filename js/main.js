// DevHub Main JavaScript
// Comprehensive application logic and event handling

// ============================================================================
// UTILITIES
// ============================================================================

// Form validation helpers
function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

function validatePassword(password) {
    return password.length >= 8 && /[A-Z]/.test(password) && /[a-z]/.test(password) && /[0-9]/.test(password);
}

function showAlert(message, type = 'success') {
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type}`;
    alertDiv.textContent = message;
    alertDiv.style.position = 'fixed';
    alertDiv.style.top = '80px';
    alertDiv.style.right = '20px';
    alertDiv.style.zIndex = '9999';
    alertDiv.style.minWidth = '300px';
    document.body.appendChild(alertDiv);
    
    setTimeout(() => {
        alertDiv.remove();
    }, 4000);
}

// ============================================================================
// SMOOTH NAVIGATION
// ============================================================================

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const href = this.getAttribute('href');
        if (href !== '#' && href !== '#forgot-password') {
            e.preventDefault();
            const target = document.querySelector(href);
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        }
    });
});

// ============================================================================
// MOBILE MENU TOGGLE
// ============================================================================

const menuToggle = document.querySelector('.mobile-menu-toggle');
const nav = document.querySelector('nav');

if (menuToggle) {
    menuToggle.addEventListener('click', () => {
        nav.classList.toggle('active');
    });
}

// Close menu when a link is clicked
if (nav) {
    nav.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', () => {
            nav.classList.remove('active');
        });
    });
}

// ============================================================================
// FORM HANDLERS
// ============================================================================

// Login form handler
function handleLogin(event) {
    event.preventDefault();
    
    const email = document.getElementById('email')?.value.trim();
    const password = document.getElementById('password')?.value;
    
    if (!email || !password) {
        showAlert('Please fill in all fields', 'warning');
        return false;
    }
    
    if (!validateEmail(email)) {
        showAlert('Please enter a valid email address', 'warning');
        return false;
    }
    
    if (password.length < 6) {
        showAlert('Password must be at least 6 characters', 'warning');
        return false;
    }
    
    showAlert('Login successful! Redirecting...', 'success');
    console.log('Login form submitted:', { email });
    
    // Simulate API call
    setTimeout(() => {
        // window.location.href = 'dashboard.html';
    }, 1500);
    
    return false;
}

// Signup form handler
function handleSignup(event) {
    event.preventDefault();
    
    const firstname = document.getElementById('firstname')?.value.trim();
    const lastname = document.getElementById('lastname')?.value.trim();
    const email = document.getElementById('email')?.value.trim();
    const password = document.getElementById('password')?.value;
    const confirm = document.getElementById('confirm')?.value;
    const terms = document.querySelector('input[name="terms"]')?.checked;
    
    if (!firstname || !lastname || !email || !password || !confirm) {
        showAlert('Please fill in all required fields', 'warning');
        return false;
    }
    
    if (!validateEmail(email)) {
        showAlert('Please enter a valid email address', 'warning');
        return false;
    }
    
    if (password.length < 8) {
        showAlert('Password must be at least 8 characters', 'warning');
        return false;
    }
    
    if (!/[A-Z]/.test(password) || !/[a-z]/.test(password) || !/[0-9]/.test(password)) {
        showAlert('Password must contain uppercase, lowercase, and numbers', 'warning');
        return false;
    }
    
    if (password !== confirm) {
        showAlert('Passwords do not match', 'warning');
        return false;
    }
    
    if (!terms) {
        showAlert('You must agree to the terms of service', 'warning');
        return false;
    }
    
    showAlert('Account created successfully! Redirecting...', 'success');
    console.log('Signup form submitted:', { firstname, lastname, email });
    
    // Simulate API call
    setTimeout(() => {
        // window.location.href = 'dashboard.html';
    }, 1500);
    
    return false;
}

// Contact form handler
function handleContactForm(event) {
    event.preventDefault();
    
    const name = document.getElementById('name')?.value.trim();
    const email = document.getElementById('email')?.value.trim();
    const subject = document.getElementById('subject')?.value.trim();
    const message = document.getElementById('message')?.value.trim();
    
    if (!name || !email || !subject || !message) {
        showAlert('Please fill in all required fields', 'warning');
        return false;
    }
    
    if (!validateEmail(email)) {
        showAlert('Please enter a valid email address', 'warning');
        return false;
    }
    
    showAlert('Message sent successfully! We will get back to you soon.', 'success');
    console.log('Contact form submitted:', { name, email, subject, message });
    
    // Reset form
    event.target.reset();
    return false;
}

// ============================================================================
// COUNTER FUNCTIONALITY
// ============================================================================

let counterValue = 0;

function initCounter() {
    const decreaseBtn = document.getElementById('decrease');
    const increaseBtn = document.getElementById('increase');
    const resetBtn = document.getElementById('reset');
    const counterDisplay = document.getElementById('counter-display') || document.getElementById('Counter');
    
    if (!decreaseBtn || !increaseBtn || !resetBtn || !counterDisplay) {
        return;
    }
    
    decreaseBtn.addEventListener('click', () => {
        counterValue--;
        updateCounterDisplay(counterDisplay);
    });
    
    increaseBtn.addEventListener('click', () => {
        counterValue++;
        updateCounterDisplay(counterDisplay);
    });
    
    resetBtn.addEventListener('click', () => {
        counterValue = 0;
        updateCounterDisplay(counterDisplay);
    });
}

function updateCounterDisplay(element) {
    if (element) {
        element.textContent = counterValue;
    }
}

// ============================================================================
// DOCUMENT READY
// ============================================================================

document.addEventListener('DOMContentLoaded', function() {
    console.log('DevHub loaded successfully');
    initCounter();
});
