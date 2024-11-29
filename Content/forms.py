from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    # Дополнительные поля, если необходимо
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']  # Можете добавить другие поля, если нужно
