from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=255, null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_name = models.CharField(max_length=255, null=True)
    product_price = models.FloatField()
    stock = models.IntegerField()
    product_description = models.TextField()
    product_image = models.FileField(upload_to="static/uploads", null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.product_name
