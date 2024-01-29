from django.shortcuts import render, redirect
from product.models import Product
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm

# Create your views here.


def index(request):
    products = Product.objects.all().order_by("-id")[:8]
    context = {
        "products": products,
    }
    return render(request, "users/index.html", context)


def product_details(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {
        "product": product,
    }
    return render(request, "users/productdetails.html", context)


def products(request):
    products = Product.objects.all().order_by("-id")
    context = {
        "products": products,
    }
    return render(request, "users/products.html", context)


# to register user


def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Succesfully registered")
            return redirect("/register")
        else:
            messages.add_message(request, messages.ERROR, "Verify form fields")
            return render(request, "users/register.html", {"forms": form})

    context = {
        "forms": UserCreationForm,
    }
    return render(request, "users/register.html", context)


# login process


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data["username"], password=data["password"]
            )
            if user is not None:
                login(request, user)
                if user.is_staff:
                    return redirect("/admin/dashboard")
                else:
                    return redirect("/")
            else:
                messages.add_message(request, messages.ERROR, "Enter correct details")
                return render(request, "users/login.html", {"forms": form})
    context = {
        "forms": LoginForm,
    }
    return render(request, "users/login.html", context)


def user_logout(request):
    logout(request)

    return redirect("/")
