from django.forms import ModelForm, widgets
from user_profile.models import Profile
from django import forms
from django_countries.widgets import CountrySelectWidget
from creditcards.forms import CardNumberField, CardExpiryField, SecurityCodeField

class ContactInfoForm(ModelForm):
    class Meta:
        model = Profile
        exclude = { 'id', 'phone', 'image' }
        widgets = {
            'name': widgets.TextInput(attrs= {'class':'form-control'}),
            'address': widgets.TextInput(attrs= {'class':'form-control'}),
            'country': CountrySelectWidget(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'postal': widgets.NumberInput(attrs={'class': 'form-control'})
        }

class ContactInfoForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput())
    number = forms.CardNumberField(label='Card Number')
    cvc = forms.SecurityCodeField(label='CVV/CVC')
    cc_expiry = CardExpiryField(label='Expiration Date')
    