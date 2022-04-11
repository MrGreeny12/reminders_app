from django.urls import path, include

from user import views

urlpatterns = [
    path("sign-in/", views.SignInView.as_view(), name="sign_in"),
]
