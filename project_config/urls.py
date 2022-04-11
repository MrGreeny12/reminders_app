from django.contrib import admin
from django.urls import path, include

from core import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home_page"),
    path("admin/", admin.site.urls),
    path("users/", include("user.urls")),
]
