from django.urls import path
from .views import *

urlpatterns = [
    path("", index),
    path("productdetails/<int:product_id>", product_details),
    path("productlist/", products),
    path("register/", register_user),
    path("login/", user_login),
    path("logout/", user_logout),
    path("productlist/login/", user_login),
    path("productlist/logout/", user_logout),
]
