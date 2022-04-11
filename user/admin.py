from django.contrib import admin

from user.models import UserModel, Settings


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "first_name", "last_name")


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ("reminders_type", "photo", "timezone", "telegram_id")
