from django.contrib.auth import authenticate, login
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from user.forms import SignInForm


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
