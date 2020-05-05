from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# adding the modules needed
from captain_console.models import Product, ProductImage, User



# Create your views here.
def index(request):
    return render(request, 'captain/index.html')

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
    # context = {'products': Product.objects.all()}
    # return render(request, 'captain/index.html', context)
