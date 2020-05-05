from django.contrib import admin
from captain_console.models import User, ProductCategory, Product, ProductImage, Cart, Order


# Register your models here.
admin.site.register(User)
admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Cart)
admin.site.register(Order)