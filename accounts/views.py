from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import LoginForm
from django.contrib.auth.forms import AuthenticationForm


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')  # Redirect to a home page or dashboard
            else:
                form.add_error(None, "Invalid username or password")
    else:
        form = LoginForm()

    return render(request, 'templates/login.html', {'form': form})
