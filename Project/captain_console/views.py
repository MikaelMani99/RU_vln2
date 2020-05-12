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
        product_ls = Product.objects.filter(category=kwargs['category'])
        page = 'captain/product_category.html'
    else:
        product_ls = {'consoles': Product.objects.filter(category=1),
                      'games': Product.objects.filter(category=2),
                      'accessories': Product.objects.filter(category=3),
                      'posters': Product.objects.filter(category=4)
                      }
        print (product_ls)
        page = 'captain/index.html'
    context = {'products': product_ls}
    return render(request, page, context)

