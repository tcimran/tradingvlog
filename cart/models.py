from django.db import models
from proj1.models import *
# Create your models here.



class cartlist(models.Model):
    cart_id=models.CharField(max_length=250)
    cart_dt=models.DateField(null=False,auto_now=True)

    def __str__(self):
        return self.cart_id

class items(models.Model):
    prodt=models.ForeignKey(product,on_delete=models.CASCADE)
    cart=models.ForeignKey(cartlist,on_delete=models.CASCADE)
    quant=models.IntegerField()
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.prodt

    def total(self):
        return self.prodt.price*self.quant

    def vat(self):
        return (self.quant.price*self.quant*(5/100))