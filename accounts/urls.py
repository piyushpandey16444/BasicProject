from django.urls import path
from .views import home_view, about_view, product_view, customer_view

urlpatterns = [
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('products/', product_view, name='products'),
    path('customers/', customer_view, name='customers'),
]
