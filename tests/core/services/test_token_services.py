import pytest

from core.services.token_services import ResetPasswordToken

pytestmark = pytest.mark.django_db


class TestResetPasswordToken:
    def test_generate_token(self):
        data = {"email": "test@test.com"}
        token = ResetPasswordToken(payload_data=data)
        assert data == token.payload_data, "Generate token error."
