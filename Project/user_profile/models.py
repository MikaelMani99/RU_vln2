from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.
class Profile(models.Model ):
    user_id = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=30)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    image = models.ImageField(upload_to='profile_image/', blank=True)

    def __str__(self):
        return self.full_name

class ProfileImage(models.Model):
    image = models.CharField(max_length=999)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class History(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    search = models.CharField(max_length=255, default="")
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_id + ": " + self.time_stamp
