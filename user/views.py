from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import PermissionDenied
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from core.services.token_services import ResetPasswordToken
from user.forms import (
    SignInForm,
    SignUpForm,
    ForgotPasswordForm, ResetPasswordForm
)
from user.models import UserModel


class SignInView(View):
    """Sign in page for users."""

    def get(self, request: HttpRequest) -> HttpResponse:
        if request.user.is_authenticated:
            return redirect("home_page")
        return render(request=request, template_name="user/sign_in.html")

    def post(self, request: HttpRequest) -> HttpResponse:
        form = SignInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=email, password=password)
            if user and user.is_active:
                login(request, user)
                return redirect("home_page")
            else:
                return render(request=request, template_name="user/sign_in.html")
        else:
            context = {
                "msg": "Invalid email or password entered"
            }
            return render(request=request, template_name="user/sign_in.html", context=context)


class SignUpView(View):
    """Sign up page for users."""

    def get(self, request: HttpRequest) -> HttpResponse:
        if request.user.is_authenticated:
            return redirect("home_page")
        return render(request=request, template_name="user/sign_up.html")

    def post(self, request: HttpRequest) -> HttpResponse:
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("users:sign_in")
        else:
            context = {
                "msg": "Invalid data, please try again"
            }
            return render(request=request, template_name="user/sign_up.html", context=context)


class SignOutView(View):
    """Sign out page for users."""

    def get(self, request: HttpRequest) -> HttpResponse:
        if not request.user.is_authenticated:
            return redirect("home_page")
        context = {
            "username": request.user.username
        }
        return render(request=request, template_name="user/sign_out.html", context=context)

    def post(self, request: HttpRequest) -> HttpResponse:
        if "sign_out" in request.POST:
            logout(request)
            return redirect(to="home_page")
        elif "cancel" in request.POST:
            return redirect(to="home_page")
        else:
            raise PermissionDenied


class ForgotPasswordView(View):
    """Forgot password page for users."""

    def get(self, request: HttpRequest) -> HttpResponse:
        if request.user.is_authenticated:
            return redirect(to="home_page")
        return render(request=request, template_name="user/forgot_password.html")

    def post(self, request: HttpRequest) -> HttpResponse:
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            user = UserModel.get_user_by_email(email=email)
            if user:
                # TODO: RELEASE - test on release email credentials
                # send_forgot_password_email()
                return redirect(to="users:success_forgot_password")
        context = {
            "message": "We don’t know this e-mail... Let’s try again!"
        }
        return render(request=request, template_name="user/forgot_password.html", context=context)


class SuccessForgotPasswordView(View):
    """Success forgot password page for users."""

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request=request, template_name="user/success_forgot_password.html")

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(to="home_page")


class ResetPasswordView(View):
    """Reset password page for users."""

    def get(self, request: HttpRequest, token: str) -> HttpResponse:
        token = ResetPasswordToken(token=token)
        if request.user.is_authenticated:
            try:
                token.validate_user(user=request.user)
                context = {"user_email": token.payload_data.get("email")}
                return render(request=request, template_name="user/reset_password.html", context=context)
            except PermissionDenied:
                return redirect("home_page")
        else:
            context = {"user_email": token.payload_data.get("email")}
            return render(request=request, template_name="user/reset_password.html", context=context)

    def post(self, request: HttpRequest, token: str) -> HttpResponse:
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="users:success_reset_password")
        context = {
            "message": "The passwords do not match. Let’s try again!"
        }
        return render(request=request, template_name="user/reset_password.html")


class SuccessResetPasswordView(View):
    """Success reset password page for users."""

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request=request, template_name="user/success_reset_password.html")

    def post(self, request: HttpRequest) -> HttpResponse:
        return redirect(to="home_page")
