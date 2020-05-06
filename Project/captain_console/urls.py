from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="captain_console_index"),
    path('consoles/', views.index, kwargs={'category': 1}, name="category_consoles"),
    path('games/', views.index, kwargs={'category': 2}, name="category_games"),
    path('accessories/', views.index, kwargs={'category': 3}, name="category_accessories"),
    path('product/<int:id>', views.get_product_by_id, name="product_details"),
    path('consoles/product/<int:id>', views.get_product_by_id, name="product_details"), # TODO: find a better solution to this.
    path('games/product/<int:id>', views.get_product_by_id, name="product_details"), # TODO: and this.
    path('accessories/product/<int:id>', views.get_product_by_id, name="product_details"), # TODO: also this.
    path('profile/<int:id>', views.get_profile_by_id, name="profile_page")
]   # path(route, view, kwargs=None, name=None)
