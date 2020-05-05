from django.shortcuts import render

from django.http import HttpResponse
from captain_console.models import Product, ProductImage


def index(request, **kwargs):
    if 'category' in kwargs:
        cat = kwargs['category']
        product = list(Product.objects.filter(category=cat))
        context = {'products': product}
        return render(request, 'captain/index.html', context)
    context = {'products': Product.objects.all()}
    return render(request, 'captain/index.html', context)

def profile(request):
    return render(request, 'captain/profile.html')

