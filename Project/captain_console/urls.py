from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="captain_console_index"),
    path('product/<int:id>', views.get_product_by_id, name="product_details"),
    path('profile/<int:id>', views.get_profile_by_id, name="profile_page")
]