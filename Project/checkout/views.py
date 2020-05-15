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
    name_location = string_data.find('name')
    contact_data = string_data[name_location:-1].split("&")
    ret_dict = dict()
    for info in contact_data:
        info = info.split("=")
        print(info)
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
    # Take in data in form
    if request.method == 'POST':
        form = ContactInfoForm(data=request.POST)
        if form.is_valid():
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

    if request.user.id == None:
        user = {}
    else:
        user = Profile.objects.filter(user_id=request.user).first()

    return render(request, 'chest/checkout_review_info.html', {'cart': cart, 'user': user})

# The confirmation page
def thank_you(request):
    return render(request, 'chest/thank_you_page.html')
