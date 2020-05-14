from django import forms
from product.models import ProductCategory, ProductType

ORDER = [
    ('name', 'Name'),
    ('price', 'Price'),
    ('amount', 'Amount')
    ]

DISCOUNT = [
    ('0', 'On sale or not?'),
    ('True', 'On sale'),
    ('False', 'Not on sale')
]

class OrderFilter(forms.Form):
    categories = ProductCategory.objects.all()
    filter_choices = [(str(c.id), c.name) for c in categories]
    filter_choices.insert(0, ('0', 'Category'))

    types = ProductType.objects.all()
    filter_type_choices = [(str(t.id), t.name) for t in types]
    filter_type_choices.insert(0, ('0', 'Type'))
    ORDER = forms.CharField(widget=forms.RadioSelect(choices=ORDER), initial=('name', 'Name'))
    FILTER = forms.CharField(widget=forms.Select(choices=filter_choices))
    FILTER_TYPE = forms.CharField(widget=forms.Select(choices=filter_type_choices))
    FILTER_DISCOUNT = forms.CharField(widget=forms.Select(choices=DISCOUNT))

    class Media:
        css = {
            'all': ('main.css',)
        }
        # js = ('animations.js', 'actions.js')

    # def __init__(self, *args, **kwargs):
    #     super(OrderFilter, self).__init__(*args, **kwargs)
    #     self.fields["SEARCH"].initial = "Some initial value"
