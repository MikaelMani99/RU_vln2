from django import forms

ORDER = [
    ('name', 'Name'),
    ('price', 'Price'),
    ]
class CHOICES(forms.Form):
    ORDER = forms.CharField(widget=forms.RadioSelect(choices=ORDER))
    class Media:
        css = {
            'all': ('main.css',)
        }
        # js = ('animations.js', 'actions.js')
