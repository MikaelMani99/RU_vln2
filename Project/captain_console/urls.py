from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="captain_console_index"),
<<<<<<< HEAD
    #path('product/<int:id>', views.get_product_by_id, name="product_details"),
    path('products/', views.get_all_products, name="product_details"),
    path('profile/<int:id>', views.get_profile_by_id, name="profile_page"),
    path('cart/', views.get_cart, name="cart_page"),
    path('cart/<int:id>', views.update_cart, name="update_cart")
]
=======
    path('consoles/', views.index, kwargs={'category': 1}, name="category_consoles"),
    path('games/', views.index, kwargs={'category': 2}, name="category_games"),
    path('accessories/', views.index, kwargs={'category': 3}, name="category_accessories"),
    path('product/<int:id>', views.get_product_by_id, name="product_details"),
    path('profile/<int:id>', views.get_profile_by_id, name="profile_page"),
    path('search/', views.search_page, name="search_page")
]   # path(route, view, kwargs=None, name=None)
>>>>>>> master
