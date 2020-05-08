from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.get_product_by_id, name="product_details")
]