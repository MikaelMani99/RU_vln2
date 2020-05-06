from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="captain_console_index"),
    path('profile/<int:id>', views.get_profile_by_id, name="profile_page")
]