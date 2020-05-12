from django.db import models

# Create your models here.


class ProductCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ProductType(models.Model):
    name = models.CharField(max_length=255, default='Type')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=999, blank=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    type = models.ForeignKey(ProductType, on_delete=models.CASCADE, default=0)
    amount = models.IntegerField()
    price = models.IntegerField()
    on_sale = models.BooleanField(default=False)
    discount = models.IntegerField(default=0)

    def getPrice(self):
        if self.on_sale:
            sale_price = round(((self.price / 100) * (1 - (self.discount / 100))), 2)
            return "NOW: ${}".format(sale_price)
        return "${}".format(self.price / 100)

    def getDiscount(self):
        return "{}%".format(self.discount)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    image = models.CharField(max_length=999)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name