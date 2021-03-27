from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Product, Customer, Tag, Order
from .forms import CustomerForm


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


def customer_view(request, id):
    try:
        customer = Customer.objects.get(id=id)
    except Customer.DoesNotExist:
        raise Http404("Customer does not exist")
    orders = customer.order_set.all()
    total_orders = orders.count()
    context = {
        'customer': customer, 
        'orders': orders,
        'total_orders': total_orders
        }
    return render(request, 'accounts/customers.html', context=context)


def create_customer(request):
    pass
