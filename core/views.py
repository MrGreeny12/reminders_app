from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View


class HomeView(View):
    """Home page for all users."""

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request=request, template_name="service_pages/home.html")
