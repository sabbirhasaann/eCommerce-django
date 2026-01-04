from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegistrationForm
from .models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = authenticate(request, username=form.cleaned_data['email'], password=form.cleaned_data['password'])
        if user:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'login.html', {'form': form})

def login_overlay(request):
    return render(request, 'login_overlay.html')

def register_view(request):
    form = RegistrationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        return redirect('login')
    return render(request, 'register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')



@login_required(login_url='/accounts/login/')
def dashboard_view(request):
    """Dashboard of user"""
    return render(request, "dashboard.html")