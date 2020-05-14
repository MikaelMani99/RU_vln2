from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from product.models import Product, ProductImage,  ProductCategory
from search.views import search_page
from .forms import ContactUsForm
from django.core.mail import EmailMessage
from django.template.loader import get_template

def index(request, **kwargs):
    if 'search_filter' in request.GET:
        return search_page(request)
    if 'category' in kwargs:
        products = Product.objects.filter(category=kwargs['category'])
        page = 'products/product_category.html'
    else:
        products = {
                    'consoles': Product.objects.filter(category=1),
                    'games': Product.objects.filter(category=2),
                    'accessories': Product.objects.filter(category=3),
                    'posters': Product.objects.filter(category=4),
                    'other': Product.objects.filter(category=5)
                    }
        page = 'captain/index.html'
    context = {'products': products}
    return render(request, page, context)

def deals(request):
    products = {
                'consoles': Product.objects.filter(category=1, on_sale=True),
                'games': Product.objects.filter(category=2, on_sale=True),
                'accessories': Product.objects.filter(category=3, on_sale=True),
                'posters': Product.objects.filter(category=4, on_sale=True),
                'other': Product.objects.filter(category=5, on_sale=True)
                }
    context = {'products': products}
    return render(request, 'captain/index.html', context)


def other(request, **kwargs):
    return render(request, 'captain/'+kwargs['site']+'.html')

def contact_us(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            # Get the form values
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            message = request.POST.get('message', '')

            print('Name: ' + contact_name)

            # Get template contact information
            template = get_template('captain/email_message.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'message': message
            }

            # Put the contact information into the template
            content = template.render(context)

            # Create email with contact template and send it
            email = EmailMessage(
                'Captain Console has received a new contact form submission',
                content,
                'Your website' + '',
                ['margretsk18@ru.is'],
                headers = {'Reply-To': contact_email}
            )
            email.send()
            return redirect('captain_console_index')

    context = {'form': ContactUsForm()}
    return render(request, 'captain/contact_us.html', context)