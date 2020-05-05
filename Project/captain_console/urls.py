from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="captain_console_index"),
    path('consoles/', views.index, kwargs={'category': 1}, name="category_consoles"),
    path('games/', views.index, kwargs={'category': 2}, name="category_games"),
    path('profile/', views.profile, name="profile_page")
]   # path(route, view, kwargs=None, name=None)