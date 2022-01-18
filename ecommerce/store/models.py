from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.name
class product(models.Model):
     name=models.CharField(max_length=200,null=True)
     price=models.FloatField()
     digital=models.BooleanField(default=False,null=True,blank=False)
     image=models.ImageField(null=True,blank=True)
     def __str__(self):
         return self.name

     @property
     def imageUrl(self):
        try:
            Url=self.image.url
        except:
            Url=''
        return Url
class order(models.Model):
    customer=models.ForeignKey(customer,on_delete=models.SET_NULL,blank=True,null=True)
    date_ordered=models.DateTimeField(auto_now_add=True)
    complete=models.BooleanField(default=False,null=True,blank=False)
    transaction_id = models.CharField(max_length=200, null=True)
    def __str__(self):
        return str(self.transaction_id)
    @property
    def shipping(self):
        shipping=False
        orderitems=self.order_item_set.all()
        for i in orderitems:
            if(i.product.digital==False):
                shipping=True
        return shipping
 

    @property
    def get_cart_total(self):
        orderitem=self.order_item_set.all()
        total=sum([item.get_total for item in orderitem])
        return total
    @property
    def get_cart_items(self):
        orderitem=self.order_item_set.all()
        total=sum([item.quantity for item in orderitem])
        return total
class order_item(models.Model):
    product=models.ForeignKey(product,on_delete=models.SET_NULL,blank=True,null=True)
    order = models.ForeignKey(order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity=models.IntegerField(default=0,null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.product.name)
    @property
    def get_total(self):
        total=self.product.price * self.quantity
        return total
class ShippingAddress(models.Model):
    customer=models.ForeignKey(customer,on_delete=models.SET_NULL,blank=True,null=True)
    order = models.ForeignKey(order, on_delete=models.SET_NULL, blank=True, null=True)
    adress = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.adress)