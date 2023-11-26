# treasure_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.treasure_island, name='treasure_island'),
]
