from django.forms import ModelForm, widgets
from user_profile.models import Profile
from django import forms
from django_countries.widgets import CountrySelectWidget
from django_countries import Countries
from creditcards.forms import CardNumberField, CardExpiryField, SecurityCodeField

class ContactInfoForm(ModelForm):
    city = forms.CharField(widget=widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}), label='')
    postal_code = forms.IntegerField(widget=widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Zip code'}), label='')

    class Meta:
        model = Profile
        exclude = {'id', 'image', 'user_id'}
        fields = ['country', 'full_name', 'phone', 'address', 'city', 'postal_code']
        widgets = {
            'country': CountrySelectWidget(attrs={'class': 'form-control'}),
            'full_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'phone': widgets.TextInput(attrs={'class': 'form-control'}),
            'address': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Street address, apartment, suite, floor, etc'})
        }

class PaymentInfoForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cardholder name'}))
    number = CardNumberField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Card number'}))
    cvc = SecurityCodeField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CVC/CVV'}))
    expiry = CardExpiryField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'MM/YY'}))
    class Media:
        css = {
            'all': ('main.css',)
        }
    