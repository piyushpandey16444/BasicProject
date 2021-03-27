from django.urls import path
from .views import *

urlpatterns = [
    path('', home_view, name='home'),
    path('products/', product_view, name='product'),
    path('customer/<int:id>/', customer_view, name='customer'),

    path('create-customer/', create_customer, name="create-customer"),
    path('create-order/', create_order, name="create-order"),
    path('update-customer/<int:id>/', update_customer, name="update-customer"),
    path('update-order/<int:id>/', update_order, name="update-order"),
    
    path('delete-customer/<int:id>/', delete_customer, name="delete-customer"),
]
