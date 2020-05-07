from django import forms
from captain_console.models import ProductCategory

ORDER = [
    ('name', 'Name'),
    ('price', 'Price'),
    ]

class OrderFilter(forms.Form):
    categories = ProductCategory.objects.all()
    filter_choices = [(str(c.id), c.name) for c in categories]
    filter_choices.insert(0, ('0', 'Category'))

    ORDER = forms.CharField(widget=forms.RadioSelect(choices=ORDER))
    FILTER = forms.CharField(widget=forms.Select(choices=filter_choices))

    class Media:
        css = {
            'all': ('main.css',)
        }
        # js = ('animations.js', 'actions.js')
