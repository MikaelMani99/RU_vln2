from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# adding the modules needed
from captain_console.models import Product, ProductImage, User, ProductCategory, Cart, CartItem
from .forms import OrderFilter


def index(request, **kwargs):
    if 'search_filter' in request.GET:
        return search_page(request)
    if 'category' in kwargs:
        product_ls = Product.objects.filter(category=kwargs['category'])
    else:
        product_ls = list(Product.objects.all())
    context = {'products': product_ls}
    return render(request, 'captain/index.html', context)


def search_page(request):
    search_filter = request.GET.get('search_filter')
    products = Product.objects.filter(name__icontains=search_filter)
    form = OrderFilter(request.POST)
    if form.is_valid():
        selected_filter = form.cleaned_data.get("FILTER")
        if is_valid_query_param(selected_filter) and selected_filter != 'Category':
            products = products.filter(category=selected_filter)
        selected_order = form.cleaned_data.get("ORDER")
        if is_valid_query_param(selected_order):
            products = products.order_by(selected_order)
    context = {
                'products': products,
                'form': form,
    }
    return render(request, 'captain/search_page.html', context)


def is_valid_query_param(param):
    return param != '' and param is not None


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


def update_cart(request, id):
    request.session.set_expiry(172800)
    try:
        qty = request.GET.get('qty')
        update_qty = True
    except:
        qty = None
        update_qty = False

    try:
        cart_id = request.session['id_of_cart']
    except:
        new_cart = Cart()
        new_cart.save()
        request.session['id_of_cart'] = new_cart.id
        cart_id = new_cart.id

    cart = Cart.objects.get(id=cart_id)

    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        pass
    except:
        pass

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if created:
        print("woo")

    if update_qty and qty:
        if int(qty) == 0:
            cart_item.delete()
        else:
            cart_item.quantity = qty
            cart_item.save()
    else:
        pass

    total_of_cart = 0
    for item in cart.cartitem_set.all():
        line_total = item.product.price * item.quantity
        total_of_cart += line_total

    request.session['total_items'] = cart.cartitem_set.count()
    cart.total = total_of_cart
    cart.save()

    return HttpResponseRedirect(reverse("cart_page"))

# fetches the product using a dynamic parameter like
# /captain/product/1
def get_product_by_id(request, id):
    return render(request, 'captain/product_details.html', {
        'product': get_object_or_404(Product, pk=id)
    })


def get_profile_by_id(request, id):

    return render(request, 'captain/profile.html', {
        'user': get_object_or_404(User, pk=id)
    })


def get_all_products(request):
    return render(request, 'captain/product_details.html', {
        'products': Product.objects.all()
    })
