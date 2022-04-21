from django.urls import path

from user import views

app_name = 'users'
urlpatterns = [
    path("sign-in/", views.SignInView.as_view(), name="sign_in"),
    path("sign-up/", views.SignUpView.as_view(), name="sign_up"),
    path("sign-out/", views.SignOutView.as_view(), name="sign_out"),
    path("forgot-password/", views.ForgotPasswordView.as_view(), name="forgot_password"),
    path("success-forgot-password/", views.SuccessForgotPasswordView.as_view(), name="success_forgot_password"),
    path("reset-password/<str:token>/", views.ResetPasswordView.as_view(), name="reset_password"),
    path("success-reset-password/", views.SuccessResetPasswordView.as_view(), name="success_reset_password"),
]
