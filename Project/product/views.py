from django.shortcuts import render, get_object_or_404

from product.models import Product, ProductImage, ProductCategory, ProductType

# Create your views here.

# fetches the product using a dynamic parameter like
# /captain/product/1
def get_product_by_id(request, id):
    return render(request, 'products/product_details.html', {
        'product': get_object_or_404(Product, pk=id)
    })

def get_all_products(request):
    return render(request, 'products/product_details.html', {
        'products': Product.objects.all()
    })
