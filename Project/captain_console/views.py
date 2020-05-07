<<<<<<< HEAD
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# adding the modules needed
from captain_console.models import Product, ProductImage, User, Cart, CartItem
=======
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
# adding the modules needed
from captain_console.models import Product, ProductImage, User
from .forms import CHOICES
>>>>>>> master

def index(request, **kwargs):
    if 'search_filter' in request.GET:
        return search_page(request)
    if 'category' in kwargs:
        product_ls = filter_by_category(kwargs['category'])
    else:
        product_ls = list(Product.objects.all())
    context = {'products': product_ls}
    return render(request, 'captain/index.html', context)

def search_page(request):
    search_filter = request.GET.get('search_filter')
    form = CHOICES(request.POST)
    if form.is_valid():
        selected = form.cleaned_data.get("ORDER")
        product_ls = list(Product.objects.filter(name__icontains=search_filter).order_by(selected))
    else:
        product_ls = list(Product.objects.filter(name__icontains=search_filter))
    context = {'products': product_ls, 'form': form}
    return render(request, 'captain/search_page.html', context)
    # render(request, '/captain/search_page.html', context)

def filter_by_category(category):
    return list(Product.objects.filter(category=category))

def filter_through_ls(ls, filter):
    new_ls = []
    for p in ls:
        if p.category.id == filter:
            new_ls.append(p)
    return new_ls


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
<<<<<<< HEAD

    # product = [{
    #     'id': p.id,
    #     'name': p.name,
    #     'description': p.description,
    #     'category': p.category,
    #     'amount': p.amount,
    #     'price':p.price,
    #     'firstImage': p.productimage_set.first().image
    # } for p in Product.objects.filter(category__icontains='console')
    # ]
    # product = list(Product.objects.filter(category__icontains='console'))
    # return JsonResponse({'data':captain})
    # context = {'products': Product.objects.all()}
    # return render(request, 'captain/index.html', context)

def get_all_products(request):
    return render(request, 'captain/product_details.html', {
        'products': Product.objects.all()
    })
=======
>>>>>>> master
