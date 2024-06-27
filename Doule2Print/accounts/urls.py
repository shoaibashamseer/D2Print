# accounts/urls.py
from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views
from .views import CustomLoginView, logout_view

urlpatterns = [
   # path('register/retail/', views.register_retail, name='register_retail'),
    #path('register/wholesale/', views.register_wholesale, name='register_wholesale'),
    path('register/', views.register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
   # path('logout/', LogoutView.as_view(next_page='login'), name='logoutView'),
    path('logout/', logout_view, name='logout'),
]
