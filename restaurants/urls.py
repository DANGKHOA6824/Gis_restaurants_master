from django.urls import path
from . import views

urlpatterns = [
    path('map/', views.map_view, name='map'),
    path('api/restaurants/', views.restaurant_json, name='restaurant_json'),
    path('restaurant/<int:pk>/', views.RestaurantDetailView.as_view(), name='restaurant_detail'),
]
