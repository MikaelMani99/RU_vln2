from django.db import models
from product.models import Product
# Create your models here.

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

class CartItem(models.Model):
    cart = models.ForeignKey('Cart', null=True, blank=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    line_total = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def getTotalPrice(self):
        return "${}".format((int(self.quantity) * int(self.product.price))/100)

    def __str__(self):
        try:
            return str(self.cart.id)
        except:
            return self.product.title