from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    #image

    def __str__(self) -> str:
        return self.name
    

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    transaction_id = models.CharField(max_length=200)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.transaction_id
    
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null= True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null= True)
    quantity = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.product.name 
    

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null= True, related_name='shipping_address')
    order =  models.ForeignKey(Customer, on_delete=models.SET_NULL, null= True)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.address
