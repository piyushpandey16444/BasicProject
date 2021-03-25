from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Customer, Tag, Order


def home_view(request):
    total_orders = Order.objects.all().count()
    total_customers = Customer.objects.all().count()
    pending_orders = Order.objects.filter(status='pending').count()
    delivered_orders = Order.objects.filter(status='delivered').count()
    customer_objs = Customer.objects.all()
    order_objs = Order.objects.all()
    context = {'customer_objs': customer_objs, 'order_objs': order_objs, 
    'total_orders': total_orders, 'delivered_orders': delivered_orders, 'pending_orders': pending_orders,}
    return render(request, 'accounts/home.html', context=context)


def product_view(request):
    product_objs = Product.objects.all()
    return render(request, 'accounts/products.html', context={'product_objs': product_objs})


def customer_view(request):
    return render(request, 'accounts/customers.html')