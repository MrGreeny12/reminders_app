from typing import Optional

from django.contrib.auth.base_user import BaseUserManager


class UserModelManager(BaseUserManager):
    """Manager for UserModel class."""
    def create_user(
        self,
        email: str,
        username: str,
        password: Optional[str] = None
    ):
        from users.models import Settings

        if not email:
            raise ValueError("Users must have an Email address")
        if not username:
            raise ValueError("Users must have an Username")
        user = self.model(email=self.normalize_email(email), username=username)

        user.set_password(password)
        user.settings = Settings.create_default_settings()
        user.save(using=self._db)
        return user

    def create_superuser(
        self,
        email: str,
        username: str,
        password: str
    ):
        user = self.create_user(email=self.normalize_email(email), password=password, username=username)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
