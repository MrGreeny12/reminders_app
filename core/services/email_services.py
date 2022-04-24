from django.conf.global_settings import DEFAULT_FROM_EMAIL
from django.core.mail import send_mail
from django.template.loader import render_to_string


def send_forgot_password_email(email: str, token: str) -> None:
    """Forgot password email sending."""
    message = render_to_string("emails/forgot_password.html", {
        "email": email,
        "token": token,
    })
    send_mail(
        subject="M.A.P.S. - Forgot password",
        message="",
        from_email=DEFAULT_FROM_EMAIL,
        recipient_list=[email],
        html_message=message
    )
