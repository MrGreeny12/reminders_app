import pytest

from user.models import UserModel

pytestmark = pytest.mark.django_db


@pytest.fixture(scope="function")
def base_user() -> UserModel:
    user = UserModel.active.create_user(
        username="test",
        email="test@test.com",
        password="123456"
    )
    yield user
