from django.db import models
from django.utils import timezone
from django.conf import settings
from django_countries.fields import CountryField


# Create your models here.
class Profile(models.Model):
    user_id = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    country = CountryField()
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    postal_code = models.IntegerField()
    image = models.ImageField(upload_to='profile_image/', blank=True)

    def __str__(self):
        return str(self.user_id)

class ProfileImage(models.Model):
    image = models.CharField(max_length=999)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class History(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    search = models.CharField(max_length=255, default="")
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_id + ": " + self.time_stamp
