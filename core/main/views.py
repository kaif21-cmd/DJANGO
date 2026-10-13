
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def home_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    return render(request, "main/home.html")


def signup_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "")
        confirm_password = request.POST.get("confirm_password", "")

        if not all([username, email, password, confirm_password]):
            messages.error(request, "All fields are required!")

        elif len(username) > 150:
            messages.error(request, "Username is too long!")

        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")

        elif User.objects.filter(email__iexact=email).exists():
            messages.error(request, "Email already registered!")

        elif len(password) < 8:
            messages.error(request, "Password must be at least 8 characters!")

        elif password != confirm_password:
            messages.error(request, "Passwords do not match!")

        else:
            User.objects.create_user(
                username=username,
                email=email,
                password=password
            )

            messages.success(
                request,
                "Signup successful! Please login."
            )
            return redirect("auth_login")

    return render(request, "main/signup.html")


def login_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")

        if not username or not password:
            messages.error(
                request,
                "Username and password are required!"
            )
        else:
            user = authenticate(
                request,
                username=username,
                password=password
            )

            if user is not None:
                login(request, user)
                return redirect("dashboard")

            messages.error(request, "Invalid username or password!")

    return render(request, "main/login.html")


@login_required(login_url="auth_login")
def dashboard_view(request):
    return render(request, "main/dashboard.html")


@login_required(login_url="auth_login")
def logout_view(request):
    if request.method == "POST":
        logout(request)
        messages.success(request, "You have logged out successfully.")
        return redirect("auth_login")

    return redirect("dashboard")
