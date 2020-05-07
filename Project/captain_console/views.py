from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# adding the modules needed
from captain_console.models import Product, ProductImage, User
from .forms import CHOICES

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
