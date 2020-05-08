from django import forms
from captain_console.models import ProductCategory, ProductType

ORDER = [
    ('name', 'Name'),
    ('price', 'Price'),
    ('amount', 'Amount')
    ]

class OrderFilter(forms.Form):
    categories = ProductCategory.objects.all()
    filter_choices = [(str(c.id), c.name) for c in categories]
    filter_choices.insert(0, ('0', 'Choose category...'))

    types = ProductType.objects.all()
    filter_type_choices = [(str(t.id), t.name) for t in types]
    filter_type_choices.insert(0, ('0', 'Choose type...'))

    ORDER = forms.CharField(widget=forms.RadioSelect(choices=ORDER))
    FILTER = forms.CharField(widget=forms.Select(choices=filter_choices))
    FILTER_TYPE = forms.CharField(widget=forms.Select(choices=filter_type_choices))

    class Media:
        css = {
            'all': ('main.css',)
        }
        # js = ('animations.js', 'actions.js')
