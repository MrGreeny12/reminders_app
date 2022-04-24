import pytest
from django.test.client import Client
from django.urls import reverse

from core.services.token_services import ResetPasswordToken
from tests.user.user_data import (
    REGISTRATION_DATA,
    LOGIN_DATA,
    EMAIL_DATA,
    RESET_PASSWORD_DATA,
    NEW_PASSWORD,
    EMAIL,
)
from user.models import UserModel

pytestmark = pytest.mark.django_db


class TestAuthViews:
    def test_sign_up_view(self, client: Client, django_user_model: UserModel):
        url = reverse("users:sign_up")
        get_response = client.get(url)
        assert get_response.status_code == 200, "Page working incorrect."

        post_response = client.post(url, data=REGISTRATION_DATA)
        assert post_response.status_code == 302, "Sign up form work incorrect."
        assert django_user_model.active.count() == 1, "User don't save in db."

    def test_sign_in_view(self, client: Client, base_user: UserModel):
        url = reverse("users:sign_in")
        get_response = client.get(url)
        assert get_response.status_code == 200, "Page working incorrect."

        post_response = client.post(url, data=LOGIN_DATA)
        assert post_response.status_code == 200, "Sign in form work incorrect."

    def test_sign_out_view(self, client: Client, base_user: UserModel):
        url = reverse("users:sign_out")
        client.force_login(base_user)
        get_response = client.get(url)
        assert get_response.status_code == 200, "Page working incorrect."

        post_response = client.post(url, {"sign_out": ""})
        assert post_response.status_code == 302, "Sign out error."

    def test_forgot_password_not_auth_view(self, client: Client, base_user: UserModel):
        url = reverse("users:forgot_password")
        get_response = client.get(url)
        assert get_response.status_code == 200, "Page working incorrect."

        post_response = client.post(url, data=EMAIL_DATA)
        assert post_response.status_code == 302, "Forgot password email work error."

    def test_forgot_password_auth_view(self, client: Client, base_user: UserModel):
        url = reverse("users:forgot_password")
        client.force_login(base_user)
        get_response = client.get(url)
        assert get_response.status_code == 302, "Redirect working incorrect."

    def test_reset_password_view(self, client: Client, base_user: UserModel, django_user_model: UserModel):
        token = ResetPasswordToken(payload_data=EMAIL_DATA)
        url = reverse("users:reset_password", kwargs={"token": token})
        get_response = client.get(url)
        assert get_response.status_code == 200, "Page working incorrect."

        post_response = client.post(url, data=RESET_PASSWORD_DATA)
        assert post_response.status_code == 302, "Reset password form error."
        update_user = django_user_model.active.get(email=EMAIL)
        assert update_user.check_password(NEW_PASSWORD), "New password don't save in db."
