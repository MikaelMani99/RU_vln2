from django.contrib import admin
from user_profile.models import Profile, History, ProfileImage
# Register your models here.
admin.site.register(Profile)
admin.site.register(ProfileImage)
admin.site.register(History)