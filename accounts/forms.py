from django import forms
from django.contrib.auth.forms import AuthenticationForm

# Use the built-in AuthenticationForm for login
class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)