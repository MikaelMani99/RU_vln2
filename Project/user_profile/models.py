from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=30)
    password = models.CharField(max_length=32)
    full_name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name

class UserImage(models.Model):
    image = models.CharField(max_length=999)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class History(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    search = models.CharField(max_length=255, default="")
    time_stamp = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.user_id + ": " + self.time_stamp