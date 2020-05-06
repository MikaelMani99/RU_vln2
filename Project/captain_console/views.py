from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# adding the modules needed
from captain_console.models import Product, ProductImage, User

def index(request, **kwargs):
    product_ls = []
    get_all = True
    if 'search_filter' in request.GET:
        product_ls = filter_name_contains(request.GET.get('search_filter'))
        get_all = False
    if 'category' in kwargs:
        if not product_ls:  # If product list is empty
            product_ls = filter_by_category(kwargs['category'])
            get_all = False
        else:
            cat = kwargs['category']
            product_ls = filter_through_ls(product_ls, cat)
            get_all = False
    if get_all:  # If product list is empty and shouldn
        product_ls = list(Product.objects.all())
    context = {'products': product_ls}
    return render(request, 'captain/index.html', context)

def filter_name_contains(filter):
    return list(Product.objects.filter(name__icontains=filter))

def filter_by_category(category):
    return list(Product.objects.filter(category=category))

def filter_through_ls(ls, filter):
    new_ls = []
    for p in ls:
        if p.category.id == filter:
            new_ls.append(p)
    return new_ls

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
