from django.contrib.auth.models import AbstractUser
from django.db import models

from reminder.models import RemindType
from user.managers import UserModelManager


class UserModel(AbstractUser):
    """Base user model."""
    # Basic fields
    email = models.EmailField(unique=True, verbose_name="Email")
    first_name = models.CharField(max_length=128, verbose_name="First name")
    last_name = models.CharField(max_length=128, verbose_name="Last name")

    # Relation fields
    settings = models.OneToOneField("user.Settings", on_delete=models.CASCADE, related_name="user_settings")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    active = UserModelManager()

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
        return cls.objects.create()
