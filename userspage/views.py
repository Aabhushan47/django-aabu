from django.shortcuts import render, redirect
from product.models import Product, Cart
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from product.forms import OrderForm

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


# logout
def user_logout(request):
    logout(request)

    return redirect("/")


@login_required
def add_to_cart(request, product_id):
    user = request.user
    product = Product.objects.get(id=product_id)

    check_item_presence = Cart.objects.filter(user=user, product=product)
    if check_item_presence:
        messages.add_message(request, messages.ERROR, "Product is already in the cart")
        return redirect("/cart")
    else:
        cart = Cart.objects.create(product=product, user=user)
        if cart:
            messages.add_message(request, messages.SUCCESS, "Product added to cart")
            return redirect("/cart")
        else:
            messages.add_message(request, messages.ERROR, "Failed to add in cart")
            return redirect("/productlist")


@login_required
def show_cart(request):
    user = request.user
    items = Cart.objects.filter(user=user)
    context = {
        "items": items,
    }
    return render(request, "users/cart.html", context)


@login_required
def delete_cart(request, cart_id):
    cart = Cart.objects.get(id=cart_id)
    cart.delete()
    messages.add_message(request, messages.SUCCESS, "Succesfully deleted")
    return redirect("/cart")


@login_required
def post_order(request, product_id, cart_id):
    user = request.user
    product = Product.objects.get(id=product_id)
    cart_item = Cart.objects.get(id=cart_id)
    context = {
        "forms": OrderForm,
    }
    return render(request, "users/orderform.html", context)
