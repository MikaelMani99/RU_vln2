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

    def getPrice(self):
        return "${}".format(self.price / 100)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    image = models.CharField(max_length=999)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name