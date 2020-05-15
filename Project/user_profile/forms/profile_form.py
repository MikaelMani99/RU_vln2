from django.forms import ModelForm, widgets, ImageField, FileInput
from user_profile.models import Profile

class ProfileForm(ModelForm):
    profile_picture = ImageField(label=('Image:'),required=False, error_messages = {'invalid':("Image files only")}, widget=FileInput)
    class Meta:
        model = Profile
        exclude = ['user_id']
        fields = ('full_name',
                  'email',
                  'address',
                  'phone',
                  'city',
                  'country',
                  'postal_code',
                  'profile_picture')
