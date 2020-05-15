import time, json, urllib
from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from product.models import Product, ProductImage, ProductCategory, ProductType
from chest.models import Cart, CartItem
from checkout.models import Order
from checkout.forms.checkout_forms import ContactInfoForm, PaymentInfoForm
from user_profile.models import Profile

def read_data(data):
    string_data = "{}".format(data)
    string_data = urllib.parse.unquote(string_data)
    name_location = string_data.find('country')
    contact_data = string_data[name_location:-1].split("&")
    ret_dict = dict()
    for info in contact_data:
        info = info.split("=")
        ret_dict[info[0]] = info[1]
    return ret_dict

def contact_info(request):
    # fetching the cart
    try:
        cart_id = request.session['id_of_cart']
        cart = Cart.objects.get(id=cart_id)
    except:
        cart_id = None
        return HttpResponseRedirect("/")
    cart = Cart.objects.get(id=cart_id)
    if request.user.id == None:
        user = {}
    else:
        user = Profile.objects.filter(user_id=request.user).first()

    items = CartItem.objects.all().filter(cart = cart)
    
    if items.count() == 0:
        return redirect('/chest/')

    if request.method == 'POST':
        form = ContactInfoForm(data=request.POST)
        if form.is_valid():
            data = read_data(request.body)
            # create order here
            order = Order()
            order.address = data['address']
            order.cart = cart
            order.city = data['city']
            order.country = data['country']
            order.full_name = data['full_name']
            order.postal_code = data['postal_code']
            order.save()
            request.session['order_id'] = order.id
            # form.save()
            return redirect("payment_info_page")
    return render(request, 'chest/checkout_contact_info.html', {
        'contact_form': ContactInfoForm(),
        'cart': cart,
        'user': user
    })

def payment_info(request):
    # fetching the cart
    try:
        cart_id = request.session['id_of_cart']
        cart = Cart.objects.get(id=cart_id)
    except:
        cart_id = None
        return HttpResponseRedirect("/")

    if request.method == 'POST':
        form = PaymentInfoForm(request.POST)
        if form.is_valid():
            return redirect("review_info_page")
        # {'payment_form': form}
    return render(request, 'chest/checkout_payment_info.html', {
        'payment_form': PaymentInfoForm(),
        'cart': cart
    })

def review_info(request):
    # fetching the cart
    try:
        cart_id = request.session['id_of_cart']
        cart = Cart.objects.get(id=cart_id)
    except:
        cart_id = None
        return HttpResponseRedirect("/")

    # grab the order 
    order_id = request.session['order_id']
    order = Order.objects.get(id=order_id)

    return  render(request, 'chest/checkout_review_info.html', {'cart': cart, 'order':order})

# The confirmation page
def confirm_purchase(request):
    try:
        cart_id = request.session['id_of_cart']
        cart = Cart.objects.get(id=cart_id)
    except:
        cart_id = None
        return HttpResponseRedirect("/")

    # grab the order 
    order_id = request.session['order_id']
    order = Order.objects.get(id=order_id)
    
    return  render(request, 'chest/thank_you_page.html', {'order':order})
