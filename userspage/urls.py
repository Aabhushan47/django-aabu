from django.urls import path
from .views import *

urlpatterns = [
    path("", index),
    path("productdetails/<int:product_id>", product_details),
    path("productlist/", products),
    path("register/", register_user),
    path("login/", user_login),
    path("logout/", user_logout),
    path("addtocart/<int:product_id>", add_to_cart),
    path("cart/", show_cart),
    path("deletecart/<int:cart_id>", delete_cart),
    path("postorder/<int:product_id>/<int:cart_id>", post_order),
]
