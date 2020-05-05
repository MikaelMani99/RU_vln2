from django.db import models


class User(models.Model):
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=30)
    password = models.CharField(max_length=32)
    full_name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)


class ProductCategory(models.Model):
    name = models.CharField(max_length=255)


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=999, blank=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    amount = models.IntegerField()
    price = models.IntegerField()


class ProductImage(models.Model):
    image = models.CharField(max_length=999)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Cart(models.Model):
    amount = models.IntegerField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)


class Order(models.Model):
    shipped = models.DateField()
    status = models.CharField(max_length=255)
    total = models.IntegerField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)