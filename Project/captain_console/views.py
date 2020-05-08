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
    else:
        product_ls = list(Product.objects.all())
    context = {'products': product_ls}
    return render(request, 'captain/index.html', context)

