from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# adding the modules needed
from captain_console.models import Product

# Create your views here.
def index(request):
    return render(request, 'captain/index.html')

# fetches the product using a dynamic parameter like
# /captain/product/1
def get_product_by_id(request, id):
    return render(request, 'captain/product_details.html', {
        'product': get_object_or_404(Product, pk=id)
    })