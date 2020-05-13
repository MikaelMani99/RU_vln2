from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="captain_console_index"),
    path('consoles/', views.index, kwargs={'category': 1}, name="category_consoles"),
    path('games/', views.index, kwargs={'category': 2}, name="category_games"),
    path('accessories/', views.index, kwargs={'category': 3}, name="category_accessories"),
    path('posters/', views.index, kwargs={'category': 4}, name="category_posters"),
    path('other/', views.index, kwargs={'category': 5}, name="category_other"),
    path('deals/', views.deals, name="deals"),
    path('about_us/', views.other, kwargs={'site': 'about_us'}, name="about_us"),
    path('privacy_policy/', views.other, kwargs={'site': 'privacy_policy'}, name="privacy_policy"),
    path('returns/', views.other, kwargs={'site': 'returns'}, name="returns"),
    path('contact_us/', views.contact_us, name="contact_us")
]   # path(route, view, kwargs=None, name=None)
