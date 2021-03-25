from django.contrib import admin
from .models import Customer, Product, Order


class OrderInline(admin.TabularInline):
    model = Order


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'create_date', 'write_date']
    list_display_links = ['name', 'email', 'phone', 'create_date', 'write_date']
    date_hierarchy = 'create_date'
    inlines = [
        OrderInline,
        ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'create_date', 'write_date']
    list_display_links = ['name', 'price', 'category', 'create_date', 'write_date']
    date_hierarchy = 'create_date'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['status', 'create_date', 'write_date']
    list_display_links = ['status', 'create_date', 'write_date']
    date_hierarchy = 'create_date'
