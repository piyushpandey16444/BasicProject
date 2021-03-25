from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=250, null=True)
    phone = models.CharField(max_length=250, null=True)
    email = models.CharField(max_length=250, null=True)
    create_date = models.DateTimeField(auto_now=True)
    write_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    
class Product(models.Model):
    CATEGORY = (
        ('indoor', 'Indoor'),
        ('outdoor', 'Outdoor'),
    )
    name = models.CharField(max_length=250, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=250, null=True, choices=CATEGORY)
    description = models.CharField(max_length=250, null=True)
    create_date = models.DateTimeField(auto_now=True)
    write_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    )
    # customer =
    # product = 
    create_date = models.DateTimeField(auto_now=True)
    write_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS, max_length=250)
