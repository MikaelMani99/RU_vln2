from django.db import models
from user_profile.models import User
class Order(models.Model):
    shipped = models.DateField()
    status = models.CharField(max_length=255)
    total = models.IntegerField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
