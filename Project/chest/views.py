import json
import urllib
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# adding the modules needed
from chest.models import Cart, CartItem
from product.models import Product, ProductImage

def get_cart(request):
    try:
        cart_id = request.session['id_of_cart']
    except:
        cart_id = None
    if cart_id:
        cart = Cart.objects.get(id=cart_id)
        cart_status = {"cart": cart}
    else:
        empty_message = "You cart is empty"
        cart_status = {"empty": True, "empty_message": empty_message}

    return render(request, 'captain/cart.html', cart_status)


def update_cart(request):
    request.session.set_expiry(172800)
    
    # fetch the data from post request
    data_in_url_form = u'{}'.format(request.body)
    decoded_data_from_url = urllib.parse.unquote(data_in_url_form)
    location_of_cart = decoded_data_from_url.find("cart_storage") + 13
    data = json.loads(decoded_data_from_url[location_of_cart:-1])
    print(data)
    
    # fetch id of cart session, create a new one if there is none
    try:
        cart_id = request.session['id_of_cart']
    except:
        new_cart = Cart()
        new_cart.save()
        request.session['id_of_cart'] = new_cart.id
        cart_id = new_cart.id

    # fetches the cart
    cart = Cart.objects.get(id=cart_id)


    # product = Product.objects.get(id=id)
    for p in data:
        product = Product.objects.get(id = p['id'][1:])
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        cart_item.quantity = p['amount']
        cart_item.save()
    
    total_of_cart = 0
    for item in cart.cartitem_set.all():
        line_total = item.product.price * item.quantity
        total_of_cart += line_total
    request.session['total_items'] = cart.cartitem_set.count()
    cart.total = total_of_cart
    cart.save()
    
    return HttpResponseRedirect(reverse("cart_page"))