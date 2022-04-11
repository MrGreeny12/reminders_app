from django.urls import path, include

from user import views

app_name = 'users'
urlpatterns = [
    path("sign-in/", views.SignInView.as_view(), name="sign_in"),
    path("sign-up/", views.SignUpView.as_view(), name="sign_up"),
]
