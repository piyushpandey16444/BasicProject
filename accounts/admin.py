from django.contrib import admin
from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'create_date', 'write_date']
    list_display_links = ['name', 'email', 'phone', 'create_date', 'write_date']
    
