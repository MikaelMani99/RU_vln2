from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
# adding the modules needed
from captain_console.models import Product, ProductImage, User, ProductCategory
from .forms import OrderFilter


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
