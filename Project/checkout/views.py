import time, json, urllib
from django.shortcuts import render, HttpResponseRedirect, reverse
from product.models import Product, ProductImage, ProductCategory, ProductType
from chest.models import Cart, CartItem
from checkout.models import Order
from checkout.forms.checkout_forms import ContactInfoForm, PaymentInfoForm

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

# def contact_info(request):
#     try:
#         cart_id = request.session['id_of_cart']
#         cart = Cart.objects.get(id=cart_id)
#     except:
#         cart_id = None
#         return HttpResponseRedirect("/")
#
#
#     # fetches the data
#     data_in_url_form = u'{}'.format(request.body)
#     decoded_data_from_url = urllib.parse.unquote(data_in_url_form)
#     location_of_cart = decoded_data_from_url.find("cart_storage") + 13
#     data = json.loads(decoded_data_from_url[location_of_cart:-1])
#     # fetches the cart
#     cart = Cart.objects.get(id=cart_id)
#     items = CartItem.objects.all().filter(cart = cart)
#     do_not_delete = []
#     # product = Product.objects.get(id=id)
#     for p in data:
#         product = Product.objects.get(id = p['id'][1:])
#         cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
#         cart_item.quantity = p['amount']
#         cart_item.save()
#         do_not_delete.append(int(p['id'][1:]))
#     print(do_not_delete)
#     # delete items that are not in cart
#     for item in items:
#         if item.product.id not in do_not_delete:
#             item.delete()
#     # update the total of the cart
#     total_of_cart = 0
#     for item in cart.cartitem_set.all():
#         line_total = item.product.getPriceInt() * item.quantity
#         total_of_cart += line_total
#     request.session['total_items'] = cart.cartitem_set.count()
#     cart.total = total_of_cart
#     cart.save()
#
#     # create the order here, fill out the initial stuff
#     try:
#         order = Order.objects.get(cart = cart_id)
#     except:
#         order = Order()
#         order.cart_id = cart_id
#         order.save()
#     return render(request, 'chest/checkout_contact_info.html', {'cart': cart})

def contact_info(request):
    try:
        cart_id = request.session['id_of_cart']
        cart = Cart.objects.get(id=cart_id)
    except:
        cart_id = None
        return HttpResponseRedirect("/")
    cart = Cart.objects.get(id=cart_id)
    if request.method == 'POST':
        form = ContactInfoForm(data=request.POST)
        if form.is_valid():
            # form.save()
            return render(request, 'chest/checkout_payment_info.html', {
                'contact_form': form,
                'form': PaymentInfoForm(),
                'cart': cart
            })
    return render(request, 'chest/checkout_contact_info.html', {
        'form': ContactInfoForm(),
        'cart': cart
    })

# def payment_info(request):
#     try:
#         cart_id = request.session['id_of_cart']
#         cart = Cart.objects.get(id=cart_id)
#     except:
#         cart_id = None
#         return HttpResponseRedirect("/")
#
#     # fill out the rest of the order
#     try:
#         data = read_data(request.body)
#         order = Order.objects.get(cart = cart_id)
#         order.full_name = data['name']
#         order.city = data['city']
#         order.address = data['address']
#         order.postal_code = data['post_code']
#         order.country = data['country']
#         order.save()
#     except:
#         return HttpResponseRedirect("chest/checkout_contact_info.html")
#
#     return  render(request, 'chest/checkout_payment_info.html', {'cart': cart, 'order':order})

def payment_info(request):
    if request.method == 'POST':
        form = PaymentInfoForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            return render(request, 'chest/checkout_review_info.html')
    return render(request, 'chest/checkout_payment_info.html', {'form': PaymentInfoForm()})

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
