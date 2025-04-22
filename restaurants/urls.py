from django.urls import path
from . import views

urlpatterns = [
    path('map/', views.map_view, name='map'),
    path('api/restaurants/', views.restaurant_json, name='restaurant_json'),
]
