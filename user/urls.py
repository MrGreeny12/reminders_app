from django.urls import path

from user import views

app_name = 'users'
urlpatterns = [
    path("sign-in/", views.SignInView.as_view(), name="sign_in"),
    path("sign-up/", views.SignUpView.as_view(), name="sign_up"),
    path("sign-out/", views.SignOutView.as_view(), name="sign_out"),
]
