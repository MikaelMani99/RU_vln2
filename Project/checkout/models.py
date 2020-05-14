from django.db import models
from chest.models import Cart, CartItem
# Create your models here.
status_choices = (
    ("Started", "Started"),
    ("Abandoned", "Abandoned"),
    ("Finished", "Finished")
)

class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    status = models.CharField(max_length=120, choices=status_choices, default="Started")
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    full_name = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    postal_code = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    def __unicode__(self):
        return self.order_id