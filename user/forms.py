from django import forms
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404

from user.models import UserModel


class SignInForm(forms.Form):
    """Form for sign in user page."""
    email = forms.EmailField(required=True)
    password = forms.CharField(max_length=128, required=True)


class SignUpForm(forms.Form):
    """Form for sign up user page."""
    username = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(max_length=128, required=True)
    confirm_password = forms.CharField(max_length=128, required=True)

    def save(self) -> None:
        username = self.cleaned_data.get("username")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise ValidationError(message="Passwords are different. Please try again.", code=400)
        UserModel.active.create_user(username=username, email=email, password=password)


class ForgotPasswordForm(forms.Form):
    """Form for forgot password user page."""
    email = forms.EmailField(required=True)


class ResetPasswordForm(forms.Form):
    """Form for reset user password page."""
    email = forms.EmailField(required=True)
    password = forms.CharField(max_length=128, required=True)
    confirm_password = forms.CharField(max_length=128, required=True)

    def save(self) -> None:
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise ValidationError(message="Passwords are different. Please try again.", code=400)
        update_user = get_object_or_404(UserModel, email=email)
        update_user.set_password(raw_password=password)
        update_user.save()
