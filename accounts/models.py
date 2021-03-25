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
    STATUS = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    )
    name = models.CharField(max_length=250, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=250, null=True, choices=CATEGORY)
    description = models.CharField(max_length=250, null=True)
    status = models.CharField(choices=STATUS, max_length=250, default='active')
    create_date = models.DateTimeField(auto_now=True)
    write_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=250, null=True)


class Order(models.Model):
    STATUS = (
        ('placed', 'Placed'),
        ('confirmed', 'Confirmed'),
        ('dispatched', 'Dispatched'),
        ('delivered', 'Delivered'),
    )
    customer = models.ForeignKey("accounts.Customer", on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey("accounts.Product", on_delete=models.SET_NULL, null=True)
    create_date = models.DateTimeField(auto_now=True)
    write_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS, max_length=250, null=True)
    tags = models.ManyToManyField("accounts.Tag")
