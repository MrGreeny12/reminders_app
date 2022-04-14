from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ObjectDoesNotExist
from django.db import models

from reminder.models import RemindType
from user.managers import UserModelManager


class UserModel(AbstractUser):
    """Base user model."""
    # Basic fields
    email = models.EmailField(unique=True, verbose_name="Email")

    # Relation fields
    settings = models.OneToOneField("user.Settings", on_delete=models.CASCADE, related_name="user_settings")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    active = UserModelManager()

    @classmethod
    def get_user_by_email(cls, email: str):
        """Get user based email."""
        try:
            user = cls.active.get(email=email, is_active=True)
            return user
        except ObjectDoesNotExist:
            return None

    def __str__(self):
        return f"{self.first_name} {self.last_name}({self.email})"


class Settings(models.Model):
    """User settings model."""
    # Basic fields
    reminders_type = models.CharField(
        max_length=10,
        choices=RemindType.choices,
        default=RemindType.OTHER,
        verbose_name="Default reminder type"
    )
    photo = models.ImageField(verbose_name="User photo")
    timezone = models.CharField(max_length=100, default="UTC", verbose_name="Timezone")
    telegram_id = models.CharField(max_length=25, blank=True, null=True, verbose_name="Telegram ID")

    @classmethod
    def create_default_settings(cls):
        settings = cls.objects.create()
        return settings

    def __str__(self):
        return f"Settings - User({self.user_settings.email})"
