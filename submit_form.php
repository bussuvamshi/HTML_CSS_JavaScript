<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Collect and sanitize input data
    $name = htmlspecialchars(trim($_POST['name']));
    $email = htmlspecialchars(trim($_POST['email']));
    $message = htmlspecialchars(trim($_POST['message']));

    // Validate input
    if (!empty($name) && !empty($email) && !empty($message)) {
        if (filter_var($email, FILTER_VALIDATE_EMAIL)) {
            // Process the form (e.g., save to database, send email, etc.)
            echo "Form submitted successfully!";
        } else {
            echo "Invalid email address.";
        }
    } else {
        echo "All fields are required.";
    }
}
?>