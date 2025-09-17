from django.urls import path
from . import views

urlpatterns = [
    path('', views.hotel_registration, name='hotel_registration'),
    path('home/', views.home, name='home'),
    
]