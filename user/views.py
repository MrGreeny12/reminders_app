from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import PermissionDenied
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from user.forms import SignInForm, SignUpForm


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

    def get(self, request):
        if not request.user.is_authenticated:
            return redirect("home_page")
        context = {
            "username": request.user.username
        }
        return render(request, "user/sign_out.html", context)

    def post(self, request):
        if "sign_out" in request.POST:
            logout(request)
            return redirect("home_page")
        elif "cancel" in request.POST:
            return redirect("home_page")
        else:
            raise PermissionDenied
