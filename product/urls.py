from django.urls import path
from .views import index,post_product,post_category,show_category,delete_category,delete_product
urlpatterns =[
    path('',index),
    path('addproduct/',post_product),
    path('addcategory/',post_category),
    path('showcategory/',show_category),
    path('deletecategory/<int:category_id>',delete_category),
    path('deleteproduct/<int:product_id>',delete_product),
]


