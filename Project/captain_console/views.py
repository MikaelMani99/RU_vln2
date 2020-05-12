from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# adding the modules needed
from product.models import Product, ProductImage,  ProductCategory
from user_profile.models import User
from search.views import search_page

def index(request, **kwargs):
    if 'search_filter' in request.GET:
        return search_page(request)
    if 'category' in kwargs:
        products = Product.objects.filter(category=kwargs['category'])
        page = 'captain/product_category.html'
    else:
        products = {
                    'consoles': Product.objects.filter(category=1),
                    'games': Product.objects.filter(category=2),
                    'accessories': Product.objects.filter(category=3),
                    'posters': Product.objects.filter(category=4)
                    }
        page = 'captain/index.html'
    context = {'products': products}
    return render(request, page, context)

def deals(request):
    products = {
                'consoles': Product.objects.filter(category=1, on_sale=True),
                'games': Product.objects.filter(category=2, on_sale=True),
                'accessories': Product.objects.filter(category=3, on_sale=True),
                'posters': Product.objects.filter(category=4, on_sale=True),
                'other': Product.objects.filter(category=5, on_sale=True)
                }
    context = {'products': products}
    return render(request, 'captain/index.html', context)


def other(request, **kwargs):
    return render(request, 'captain/'+kwargs['site']+'.html')