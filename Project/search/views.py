from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

from product.models import Product, ProductImage, ProductCategory, ProductType
from .forms import OrderFilter

def search_page(request):
    search_filter = request.GET.get('search_filter')
    products = Product.objects.filter(name__icontains=search_filter)
    form = OrderFilter(request.POST)
    if form.is_valid():
        selected = form.cleaned_data.get("FILTER")
        if is_valid_query_param(selected) and selected != '0':  # 0 is the id of 'Choose catgory...'
            products = products.filter(category=selected)
        selected = form.cleaned_data.get("FILTER_TYPE")
        if is_valid_query_param(selected) and selected != '0':  # 0 is the id of 'Choose type...'
            products = products.filter(type=selected)
        selected = form.cleaned_data.get("ORDER")
        if is_valid_query_param(selected):
            products = products.order_by(selected)
    context = {
                'products': products,
                'form': form,
    }
    return render(request, 'captain/search_page.html', context)


def is_valid_query_param(param):
    return param != '' and param is not None