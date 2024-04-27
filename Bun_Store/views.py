from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *


# Create your views here.


# Home and Accounts management
@login_required
def bun_Home(request):
    context = {"title": "Honey Bun Shop", "description": "Home page of Honey Bun Shop"}
    return render(request, "bun_home.html", context)


def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        # Validating if data is correct
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            error_message = "Invalid username or password"
            return render(request, "user_login.html", {"error_message": error_message})

    return render(request, "user_login.html")


def user_signup(request):
    context = {
        'title': 'User signup',
        'description': 'Create your account with us'
    }
    if request.method == "POST":
        username = request.POST["username"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        password = request.POST["password"]
        repeatPassword = request.POST["repeatPassword"]

        if password == repeatPassword:
            try:
                # Creating user
                user = User.objects.create_user(username, email, password)

                user.first_name = first_name
                user.last_name = last_name

                user.save()

                login(request, user, )
                return redirect("/")
            except:
                error_message = "Error creating account"
                return render(
                    request, "user_signup.html", {"error_message": error_message}, context
                )
        else:
            error_message = "Password do not match"
            return render(request, "user_signup.html", {"error_message": error_message})
    return render(request, "user_signup.html", context)


def user_logout(request):
    logout(request)
    return redirect("/")


# Store and product management
def bun_store(request):
    products = Product.objects.all()
    context = {
        "title": "Honey Bun Store",
        "products": products,
    }
    return render(request, "bun_store.html", context)
