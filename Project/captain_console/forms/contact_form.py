from django import forms

class ContactUsForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    message = forms.CharField(required=True, widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(ContactUsForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "What's your name:"
        self.fields['contact_email'].label = "What's your email address:"
        self.fields['message'].label = 'What is it you want us to know?'

