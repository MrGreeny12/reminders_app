USERNAME = "test"
EMAIL = "test@test.com"
PASSWORD = "123456"
NEW_PASSWORD = "654321"
REGISTRATION_DATA = {
    "username": USERNAME,
    "email": EMAIL,
    "password": PASSWORD,
    "confirm_password": PASSWORD
}
LOGIN_DATA = {"username": USERNAME, "password": PASSWORD}
EMAIL_DATA = {"email": EMAIL}
RESET_PASSWORD_DATA = {"password": NEW_PASSWORD, "confirm_password": NEW_PASSWORD, "email": EMAIL}
