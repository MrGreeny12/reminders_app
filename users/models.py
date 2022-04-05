from django.contrib.auth.models import AbstractUser
from django.db import models


class UserModel(AbstractUser):
    """Base user model."""
    # Basic fields
    first_name = models.CharField(max_length=128, verbose_name="First name")
    last_name = models.CharField(max_length=128, verbose_name="Last name")

    # Relation fields
    settings = models.OneToOneField("users.Settings", on_delete=models.CASCADE, related_name="user_settings")
    # TODO: create email auth

    def __str__(self):
        return f"{self.first_name} {self.last_name}({self.email})"


class Settings(models.Model):
    """User settings model."""
    # Basic fields
    reminders_type = models.CharField(
        max_length=...,
        choices=...,
        default=...,
        verbose_name="Default reminders type"
    )  # TODO: add typing after reminders create
    photo = models.ImageField(verbose_name="User photo")
    timezone = models.CharField(default='UTC', max_length=100, verbose_name="Timezone")
    telegram_id = models.CharField(blank=True, null=True, verbose_name="Telegram ID")
    # TODO: create user -> automate created user-settings
