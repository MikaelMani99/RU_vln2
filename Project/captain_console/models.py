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


    def getPrice(self):
        return "${}".format(self.price/100)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    image = models.CharField(max_length=999)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name

<<<<<<< HEAD
class CartItem(models.Model):
    cart = models.ForeignKey('Cart', null=True, blank=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    line_total = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        try:
            return str(self.cart.id)
        except:
            return self.product.title
=======
class UserImage(models.Model):
    image = models.CharField(max_length=999)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
>>>>>>> master

class Cart(models.Model):
    #items = models.ManyToManyField(CartItem, null=True, blank=True)
    total = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
    updated = models.DateTimeField(auto_now_add=True, auto_now=False)
    active = models.BooleanField(default=True)

    def getTotalPrice(self):
        return "${}".format(self.total/100)

    def __str__(self):
        return "Cart ID: %s"%self.id


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
