from django.contrib import admin

from users.models import UserModel, Settings


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "first_name", "last_name")
