from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.db.models import Q
from product.models import Product, ProductImage, ProductCategory, ProductType
from user_profile.models import History
from .forms import OrderFilter

from django.utils import timezone

def search_page(request):
    search_filter = request.GET.get('search_filter')
    products = Product.objects.filter(Q(name__icontains=search_filter) |
                                      Q(type__name__icontains=search_filter) |
                                      Q(category__name__icontains=search_filter)
                                      )
    form = OrderFilter(request.POST)
    if form.is_valid():
        products = apply_relevant_filters(form, products)
        product = [{
            'id': p.id,
            'name': p.name,
            'price': p.getPrice(),
            'firstImage': p.productimage_set.first().image,
            'on_sale': str(p.on_sale),
            'discount': p.getDiscount(),
            'discount_price': p.getDiscountPrice(),
            'category': p.category.name
        } for p in products
        ]
        return JsonResponse({'products': product})

    # Add search to history if user is logged in
    elif request.user.is_authenticated:
        history = History.objects.create(user_id=request.user, search=search_filter)
        history.save()

    context = {
                'products': products,
                'form': OrderFilter(),
    }
    return render(request, 'captain/search_page.html', context)

def apply_relevant_filters(form, products):
    selected = form.cleaned_data.get("FILTER")
    if is_valid_query_param(selected) and selected != '0':  # 0 is the id of 'Choose catgory...'
        products = products.filter(category=selected)
    selected = form.cleaned_data.get("FILTER_TYPE")
    if is_valid_query_param(selected) and selected != '0':  # 0 is the id of 'Choose type...'
        products = products.filter(type=selected)
    selected = form.cleaned_data.get("ORDER")
    if is_valid_query_param(selected):
        products = products.order_by(selected)
    return products

def is_valid_query_param(param):
    return param != '' and param is not None