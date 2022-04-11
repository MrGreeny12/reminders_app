from django import forms


class SignInForm(forms.Form):
    """Form for sign in user page."""
    email = forms.EmailField()
    password = forms.CharField(max_length=100)
