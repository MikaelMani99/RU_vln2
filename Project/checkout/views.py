import time, json, urllib
from django.shortcuts import render, HttpResponseRedirect, reverse
from product.models import Product, ProductImage, ProductCategory, ProductType
from chest.models import Cart, CartItem
from checkout.models import Order

def read_data(data):
    string_data = "{}".format(data)
    string_data = urllib.parse.unquote(string_data)
    name_location = string_data.find('name')
    contact_data = string_data[name_location:-1].split("&")
    ret_dict = dict()
    for info in contact_data:
        info = info.split("=")
        print(info)
        ret_dict[info[0]] = info[1]
    return ret_dict

def contact_info(request):
    try:
        cart_id = request.session['id_of_cart']
        cart = Cart.objects.get(id=cart_id)
    except:
        cart_id = None
        return HttpResponseRedirect("/")
    
    
    # create the order here, fill out the initial stuff
    try:
        order = Order.objects.get(cart = cart_id)
    except:
        order = Order(cart = cart_id)
        order.save()
    return render(request, 'chest/checkout_contact_info.html', {'cart': cart})

def payment_info(request):
    try:
        cart_id = request.session['id_of_cart']
        cart = Cart.objects.get(id=cart_id)
    except:
        cart_id = None
        return HttpResponseRedirect("/")
    
    # fill out the rest of the order
    try:
        data = read_data(request.body)
        order = Order.objects.get(cart = cart_id)
        order.full_name = data['name']
        order.city = data['city']
        order.address = data['address']
        order.postal_code = data['post_code']
        order.country = data['country']
        order.save()
    except:
        return HttpResponseRedirect("chest/checkout_contact_info.html")
        
    

    return  render(request, 'chest/checkout_payment_info.html', {'cart': cart, 'order':order})

def review_info(request):
    try:
        cart_id = request.session['id_of_cart']
        cart = Cart.objects.get(id=cart_id)
    except:
        cart_id = None
        return HttpResponseRedirect("/")

    try:
        order = Order.objects.get(cart = cart_id)
    except:
        order = None
        return HttpResponseRedirect("/")


    return  render(request, 'chest/checkout_review_info.html', {'cart': cart, 'order': order})

def confirm_purchase(request):
    pass
