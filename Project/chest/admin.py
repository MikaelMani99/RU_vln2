from django.contrib import admin

from chest.models import Cart, CartItem
# Register your models here.
admin.site.register(Cart)
admin.site.register(CartItem)