from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=250, null=True)
    phone = models.CharField(max_length=250, null=True)
    email = models.CharField(max_length=250, null=True)
    create_date = models.DateTimeField(auto_now=True)
    write_date = models.DateTimeField(auto_now_add=True)