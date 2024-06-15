from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
   # path('place_order/', views.place_order, name='place_order'),
   # path('update_customer/', views.update_customer, name='update_customer'),
    #path('order/<int:variety_id>/', views.order_product, name='order_product'),
]
