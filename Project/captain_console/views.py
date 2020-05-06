from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# adding the modules needed
from captain_console.models import Product, ProductImage, User

def index(request, **kwargs):
    if 'category' in kwargs:
        cat = kwargs['category']
        product = list(Product.objects.filter(category=cat))
        context = {'products': product}
        return render(request, 'captain/index.html', context)
    context = {'products': Product.objects.all()}
    return render(request, 'captain/index.html', context)

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
