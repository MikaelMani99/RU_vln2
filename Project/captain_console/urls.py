from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="captain_console_index"),
    path('consoles/', views.index, kwargs={'category': 1}, name="category_consoles"),
    path('games/', views.index, kwargs={'category': 2}, name="category_games"),
    path('accessories/', views.index, kwargs={'category': 3}, name="category_accessories")
]   # path(route, view, kwargs=None, name=None)
