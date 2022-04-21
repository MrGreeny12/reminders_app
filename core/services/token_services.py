from typing import Dict, Optional, Union

import jwt
from django.core.exceptions import PermissionDenied

from core.exceptions import InvalidTokenType
from project_config.settings import SECRET_KEY_FOR_RESET_PASSWORD
from user.models import UserModel


class TokenService:
    """
    Base Class for working with tokens.

    It takes the payload data or token as input.
    The token is generated and encoded depending on the transmitted data.
    To get the data, use the methods:
    - TokenService object.payload_data
    - TokenService object.token
    - str(TokenService object)
    """
    token_type: str
    secret_key: str
    _payload_data: Dict[str, Union[str, int]]
    _token: str

    def __init__(
        self,
        payload_data: Dict[str, Union[str, int]] = None,
        token: Optional[str] = None
    ):
        assert self.token_type, "Token type not specified"
        assert self.secret_key, "Token secret key not specified"
        if not payload_data:
            payload_data = {}
        if token:
            self._token = token
            self._payload_data = self._decode()
            self._validate_token_type()
        else:
            self._payload_data = payload_data
            self._token = self._generate()

    def __str__(self) -> str:
        """Return string format token."""
        return self._token

    @property
    def payload_data(self) -> Dict[str, Union[str, int]]:
        """Return payload data based token."""
        return self._payload_data

    @property
    def token(self) -> str:
        """Return token."""
        return self._token

    def _generate(self) -> str:
        # Generate JWT data based token-type.
        self._payload_data["type"] = self.token_type
        return jwt.encode(payload=self._payload_data, key=self.secret_key)

    def _decode(self) -> Dict[str, Union[str, int]]:
        # Decode JWT data based token-type.
        return jwt.decode(self._token, key=self.secret_key, algorithms=["HS256"])

    def _validate_token_type(self) -> None:
        # Checks the validity type of the token.
        if self._payload_data.get("type") != self.token_type:
            raise InvalidTokenType
        del self._payload_data["type"]


class ResetPasswordToken(TokenService):
    """Class for working with Firm invite-code token."""
    token_type: str = "reset_password"
    secret_key: str = SECRET_KEY_FOR_RESET_PASSWORD

    def validate_user(self, user: UserModel) -> None:
        email = self._payload_data["email"]
        token_user = UserModel.get_user_by_email(email=email)
        if token_user and token_user == user:
            pass
        else:
            raise PermissionDenied
