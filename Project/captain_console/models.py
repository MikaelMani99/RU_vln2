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
    
    def __str__(self):
        return self.full_name


class ProductCategory(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=999, blank=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    amount = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    image = models.CharField(max_length=999)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name

class Cart(models.Model):
    amount = models.IntegerField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)


class Order(models.Model):
    shipped = models.DateField()
    status = models.CharField(max_length=255)
    total = models.IntegerField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class History(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField()

    def __str__(self):
        return self.user_id + ": " + self.time_stamp
