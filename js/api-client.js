/**
 * API Client for BussuTech Backend
 * Handles all HTTP requests to the Flask API
 */

const API_BASE_URL = 'http://127.0.0.1:5000/api';

/**
 * Make HTTP request to API
 * @param {string} endpoint - API endpoint path
 * @param {string} method - HTTP method (GET, POST, PUT, DELETE)
 * @param {object} data - Request body data
 * @returns {Promise} - Response data
 */
async function apiCall(endpoint, method = 'GET', data = null) {
    try {
        const options = {
            method: method,
            headers: {
                'Content-Type': 'application/json',
            }
        };

        if (data && (method === 'POST' || method === 'PUT')) {
            options.body = JSON.stringify(data);
        }

        const response = await fetch(`${API_BASE_URL}${endpoint}`, options);
        const responseData = await response.json();

        if (!response.ok) {
            throw new Error(responseData.error || `API Error: ${response.status}`);
        }

        return responseData;
    } catch (error) {
        console.error('API Error:', error);
        throw error;
    }
}

/**
 * USER AUTHENTICATION FUNCTIONS
 */

/**
 * Register a new user
 * @param {object} userData - User registration data
 * @returns {Promise} - Registration response
 */
async function registerUser(userData) {
    return apiCall('/auth/signup', 'POST', {
        first_name: userData.firstName,
        last_name: userData.lastName,
        email: userData.email,
        password: userData.password,
        password_confirm: userData.passwordConfirm,
        newsletter: userData.newsletter || false
    });
}

/**
 * Login user
 * @param {string} email - User email
 * @param {string} password - User password
 * @returns {Promise} - Login response with user data
 */
async function loginUser(email, password) {
    return apiCall('/auth/login', 'POST', {
        email: email,
        password: password
    });
}

/**
 * Get user profile by ID
 * @param {number} userId - User ID
 * @returns {Promise} - User data
 */
async function getUserProfile(userId) {
    return apiCall(`/users/${userId}`, 'GET');
}

/**
 * CONTACT FORM FUNCTIONS
 */

/**
 * Submit contact form
 * @param {object} formData - Contact form data
 * @returns {Promise} - Submission response
 */
async function submitContactForm(formData) {
    return apiCall('/contact/submit', 'POST', {
        name: formData.name,
        email: formData.email,
        subject: formData.subject,
        category: formData.category,
        message: formData.message,
        user_id: formData.userId || null
    });
}

/**
 * Get all form submissions (admin)
 * @returns {Promise} - List of submissions
 */
async function getFormSubmissions() {
    return apiCall('/contact/submissions', 'GET');
}

/**
 * Update form submission status (admin)
 * @param {number} submissionId - Submission ID
 * @param {string} status - New status
 * @returns {Promise} - Updated submission
 */
async function updateSubmissionStatus(submissionId, status) {
    return apiCall(`/contact/submissions/${submissionId}`, 'PUT', {
        status: status
    });
}

/**
 * USER MANAGEMENT FUNCTIONS (Admin)
 */

/**
 * Get all users (admin)
 * @returns {Promise} - List of users
 */
async function getAllUsers() {
    return apiCall('/users', 'GET');
}

/**
 * Health check - verify API is running
 * @returns {Promise} - API status
 */
async function checkAPIHealth() {
    return apiCall('/health', 'GET');
}
