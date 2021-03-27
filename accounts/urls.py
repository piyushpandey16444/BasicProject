from django.urls import path
from .views import home_view, product_view, customer_view, create_customer

urlpatterns = [
    path('', home_view, name='home'),
    path('products/', product_view, name='product'),
    path('customer/<int:id>/', customer_view, name='customer'),

    path('create-customer/', create_customer, name="create-customer")
]
