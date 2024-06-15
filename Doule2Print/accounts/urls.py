# accounts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('register/retail/', views.register_retail, name='register_retail'),
    path('register/wholesale/', views.register_wholesale, name='register_wholesale'),
    path('profile/', views.profile, name='profile'),
]
