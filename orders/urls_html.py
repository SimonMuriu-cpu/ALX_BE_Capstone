from django.urls import path
from .views import orders_list, create_order

urlpatterns = [
    path('', orders_list, name='orders_list'),
    path('create/', create_order, name='create_order'),
]
