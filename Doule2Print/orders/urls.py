from django.urls import path
from . import views

urlpatterns = [
    #path('place_order/<int:variety_id>/', views.place_order, name='place_order'),
    path('place_order/', views.place_order, name='place_order'),

]
