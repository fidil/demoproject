from django.db import models
from shop.models import Product
from django.contrib.auth.models import User
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    products=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    date_added=models.DateField(auto_now_add=True)
    active=models.BooleanField(default=True)

    def __str__(self):
     return self.products.name

    def subtotal(self):
        return self.quantity*self.products.price



class Account(models.Model):
    accountno=models.CharField(max_length=20)
    acctype=models.CharField(max_length=20)
    amount=models.CharField(max_length=20)
