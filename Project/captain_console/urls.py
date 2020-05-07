from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="captain_console_index"),
    #path('product/<int:id>', views.get_product_by_id, name="product_details"),
    path('products/', views.get_all_products, name="product_details"),
    path('profile/<int:id>', views.get_profile_by_id, name="profile_page"),
    path('cart/', views.get_cart, name="cart_page"),
    path('cart/<int:id>', views.update_cart, name="update_cart")
]