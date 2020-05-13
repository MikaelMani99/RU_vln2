import time
from django.shortcuts import render, HttpResponseRedirect, reverse
from product.models import Product, ProductImage, ProductCategory, ProductType
from chest.models import Cart, CartItem
from checkout.models import Order


def contact_info(request):
    try:
        cart_id = request.session['id_of_cart']
        cart = Cart.objects.get(id=cart_id)
        print (cart)
    except:
        cart_id = None
        print ("NONE")
        return HttpResponseRedirect("/chest/")

    new_order, created = Order.objects.get_or_create(cart=cart)
    if created:
        new_order.order_id = str(time.time())
        new_order.save()
    return render(request, 'chest/checkout_contact_info.html', {})