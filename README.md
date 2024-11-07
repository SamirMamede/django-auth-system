## Django Authentication System 🔒

This is a simple authentication system built with Python and Django. The project demonstrates how to implement user registration, login, logout, and password management (reset, change) in a Django application. It follows best practices in web development, including the use of Django's built-in authentication framework.

### Features ✨

- User registration
- Login and Logout functionality
- Password reset and change
- Email-based password reset
- Session management for authenticated users
- Basic front-end templates

### Technologies Used 🛠️

- **Python**: Programming language
- **Django**: Web framework
- **SQLite**: Default database for development
- **HTML/CSS**: For the basic front-end templates

## Installation ⚙️

Follow the steps below to install and set up the project:

1. Clone the repository:
   ```bash
   git clone https://github.com/SamirMamede/django-auth-system.git
2. Navigate to the project directory.
3. Create a virtual environment (optional but recommended):
   ```bash
    python -m venv venv
    source venv/bin/activate  # For Linux/Mac
    venv\Scripts\activate  # For Windows
4. Install the dependencies:
    ```bash
    pip install -r requirements.txt
5. Run database migrations:
    ```bash
    python manage.py migrate
6. Start the development server:
    ```bash
    python manage.py runserver
7. Access the application in your browser: http://127.0.0.1:8000/

### The following routes are available in the application:

    - login/
    - logout/
    - private_page_one/
    - private_page_two/
    - password_change/
    - password_change_done/
    - password_reset/
    - password_reset_done/
    - password_reset_confirm/<uidb64>/<token>/
    - password_reset_complete/
    - register/

## Features Implementation 📝

### User Registration
The user registration feature was implemented using Django's built-in form to create new users. The system validates the input data and, upon success, creates a new user in the database. The user is redirected to a confirmation page after registration.

### Login and Logout Functionality
The login and logout system utilizes Django's integrated views. The login view authenticates the user based on the provided credentials, while the logout view ends the user's session. Both views are configured to redirect the user to the homepage or a specific page after the action.

### Password Reset and Change
For the password reset and change functionality, I used Django's password reset views. The process involves sending an email with a link to reset the password, which takes the user to a page where they can enter a new password. The password change is done through a form that validates the new password and updates it in the database.

### Email-based Password Reset
The email-based password reset feature was implemented using Django's email sending system. When a user requests a password reset, an email is sent with a unique link that allows the user to securely reset their password.

### Session Management for Authenticated Users
Session management for authenticated users is handled through Django's authentication system. The framework takes care of creating and maintaining sessions, allowing users to stay logged in while navigating the site. Private pages are protected by a decorator that checks if the user is authenticated.

### Access to Private Pages
Private pages are accessible only to authenticated users. I used the `@login_required` decorator from Django to protect these views, ensuring that only logged-in users can access them. If an unauthenticated user tries to access a private page, they are redirected to the login page.

### Basic Front-end Templates
The front-end templates were created using basic HTML and CSS. The login, registration, and password reset pages were styled to be simple, as the focus of the project was on the back-end. Django Template Language was used to render dynamic data on the pages.

## Tests Implementation 🧪

The project includes comprehensive test coverage for the authentication system. The tests are organized into three main categories:

### Views Tests
- Home page accessibility
- Private pages access (both authenticated and unauthenticated)
- Authentication redirections
- Template rendering verification

### Registration Tests
- Registration form display
- Successful user registration process
- User creation verification

### Form Tests
- Login form validation
- Registration form field validation
- Form data processing

To run the tests, use the following command:
```bash
python manage.py test accounts
```

### Contribution 🤝

If you would like to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch (git checkout -b feature/your-feature-name).
3. Make your changes and commit them (git commit -m 'Add some feature').
4. Push to the remote repository (git push origin feature/your-feature-name).
5. Open a Pull Request.