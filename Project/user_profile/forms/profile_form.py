from django.forms import ModelForm, widgets
from user_profile.models import Profile

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user_id_id']