from django.shortcuts import render

from django.http import HttpResponse
from captain_console.models import Product, ProductImage


def index(request):
    # product = [{
    #     'id': p.id,
    #     'name': p.name,
    #     'description': p.description,
    #     'category': p.category,
    #     'amount': p.amount,
    #     'price':p.price,
    #     'firstImage': p.productimage_set.first().image
    # } for p in Product.objects.filter(category__icontains='console')
    # ]
    # product = list(Product.objects.filter(category__icontains='console'))
    # return JsonResponse({'data':captain})
    context = {'products': Product.objects.all()}
    return render(request, 'captain/index.html', context)

def profile(request):
    return render(request, 'captain/profile.html')

