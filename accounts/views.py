from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Product, Customer, Tag, Order
from .forms import CustomerForm, OrderForm


def home_view(request):
    total_orders = Order.objects.all().count()
    total_customers = Customer.objects.all().count()
    pending_orders = Order.objects.filter(status='pending').count()
    delivered_orders = Order.objects.filter(status='delivered').count()
    customer_objs = Customer.objects.all()
    order_objs = Order.objects.all()[0:5]
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
    form = CustomerForm()
    if request.method == "POST":
        form = CustomerForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {"form": form}
    return render(request, 'accounts/create_form.html', context=context)


def update_customer(request, id):
    try:
        customer = Customer.objects.get(id=id)
    except Customer.DoesNotExist:
        raise Http404("Customer does not exist")
    form = CustomerForm(instance=customer)
    if request.method == "POST":
        form = CustomerForm(data=request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect(f'/customer/{customer.id}/')

    context = {"form": form}
    return render(request, 'accounts/create_form.html', context=context)


def create_order(request):
    form = OrderForm()
    if request.method == "POST":
        form = OrderForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {"form": form}
    return render(request, 'accounts/create_order_form.html', context=context)


def update_order(request, id):
    try:
        order = Order.objects.get(id=id)
    except Order.DoesNotExist:
        raise Http404("Order does not exist")
    form = OrderForm(instance=order)
    if request.method == "POST":
        form = OrderForm(data=request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {"form": form}
    return render(request, 'accounts/create_order_form.html', context=context)


def delete_customer(request, id):
    try:
        get_customer = Customer.objects.get(id=id)
    except Customer.DoesNotExist:
        raise Http404("Customer Does not Exist !")
    if request.method == "POST":
        get_customer.delete()
        return redirect('/')
    context = { 'customer': get_customer}
    return render(request, 'accounts/delete_customer.html', context=context)

    
