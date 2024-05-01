import json
import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.http import JsonResponse
from .models import *


# Create your views here.


# HOME AND ACCOUNT MANAGEMENT
@login_required
def bun_Home(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cartItems = order["get_cart_items"]
        items = []
        order = {"get_cart_total": 0, "get_cart_items": 0, "shipping": False}

    context = {
        "title": "Honey Bun Shop",
        "description": "Home page of Honey Bun Shop",
        "cartItems": cartItems,
    }

    return render(request, "bun_home.html", context)

# Login to a existing account
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

# Create an account
def user_signup(request):
    context = {"title": "User signup", "description": "Create your account with us"}
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

                login(
                    request,
                    user,
                )

                return redirect("/")
            except Exception as e:
                error_message = f"Error creating account {e}"
                print(error_message)
                return render(
                    request,
                    "user_signup.html",
                    {"error_message": error_message},
                    context,
                )
        else:
            error_message = "Password do not match"
            return render(request, "user_signup.html", {"error_message": error_message})
    return render(request, "user_signup.html", context)


def user_logout(request):
    logout(request)
    return redirect("/")


# STORE, CART, CHECKOUT AND PRODUCT MANAGEMENT 
def bun_store(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {"get_cart_total": 0, "get_cart_items": 0, "shipping": False}

        cartItems = order["get_cart_items"]

    products = Product.objects.all()
    context = {
        "items": items,
        "order": order,
        "cartItems": cartItems,
        "title": "Honey Bun Store",
        "products": products,
    }
    return render(request, "bun_store.html", context)


def bun_cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        error_message = "You need to be log in to get a cart"

        cartItems = order["get_cart_items"]
        items = []
        order = {"get_cart_total": 0, "get_cart_items": 0, "shipping": False}
        context = {
            "items": items,
            "order": order,
            "error_message": error_message,
            "cartItems": cartItems,
        }

        return render(request, "bun_cart.html", context)

    context = {
        "items": items,
        "order": order,
        "cartItems": cartItems,
    }
    return render(request, "bun_cart.html", context)


def bun_checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {"get_cart_total": 0, "get_cart_items": 0, "shipping": False}

        cartItems = order["get_cart_items"]

    context = {
        "items": items,
        "order": order,
        "cartItems": cartItems,
    }
    return render(request, "bun_checkout.html", context)


def bun_updateItem(request):
    data = json.loads(request.body)
    productId = data["productId"]
    action = data["action"]
    print(f"Action: {action}, ProductID: {productId}")

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == "add":
        orderItem.quantity = orderItem.quantity + 1
    elif action == "remove":
        orderItem.quantity = orderItem.quantity - 1

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse("Item was added", safe=False)


def bun_processOrder(request):
    print('Data', request.body)
    
    data = json.loads(request.body)
    transaction_id = datetime.datetime.now().timestamp()

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['form']['total'])
        total = round(total, 2)
        print("total:", total)
        order.transaction_id = transaction_id
        
        if total == order.get_cart_total:
            order.complete = True
        order.save()
        
        if order.shipping == True:
            ShippingAddress.objects.create(
                customer=customer,
                order=order,
                address=data['shipping']['address'],
                city=data['shipping']['state'],
                zipcode=data['shipping']['zipcode'],
            )
    else:
        print('User is not logged in')

    return JsonResponse('Payment complete!', safe=False)


def detalle_pagina(request, slug):
    pagina = get_object_or_404(Product, slug=slug)
    return render(request, 'detalle_pagina.html', {'pagina': pagina})
