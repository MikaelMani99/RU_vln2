from django.forms import ModelForm, widgets
from user_profile.models import Profile
from django import forms
from django_countries.widgets import CountrySelectWidget
from creditcards.forms import CardNumberField, CardExpiryField, SecurityCodeField

class ContactInfoForm(ModelForm):
    class Meta:
        model = Profile
        exclude = {'id', 'phone', 'image', 'user_id'}
        widgets = {
            'name': widgets.TextInput(attrs= {'class':'form-control'}),
            'address': widgets.TextInput(attrs= {'class':'form-control'}),
            'country': CountrySelectWidget(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'postal': widgets.NumberInput(attrs={'class': 'form-control'})
        }

class PaymentInfoForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput())
    number = CardNumberField(label='Card Number')
    cvc = SecurityCodeField(label='CVV/CVC')
    expiry = CardExpiryField(label='Expiration Date')
    class Media:
        css = {
            'all': ('main.css',)
        }
    