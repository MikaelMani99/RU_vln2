from django.db import models
from django.conf import settings

class Order(models.Model):
    shipped = models.DateField()
    status = models.CharField(max_length=255)
    total = models.IntegerField()
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
