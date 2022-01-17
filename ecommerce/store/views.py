import product as product
from django.shortcuts import render
from .models import *
# Create your views here.
def store(request):
    products=product.objects.all()
    context={'products':products}
    return render(request,'store/store.html',context)
def cart(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        Order,created=order.objects.get_or_create(customer=customer,complete=False)
        items=Order.order_item_set.all()
    else:
        items=[]
        Order={'get_cart_total':0,'get_cart_items':0}
    context={'items':items,'order':Order}
    return render(request,'store/cart.html',context)
def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        Order, created = order.objects.get_or_create(customer=customer, complete=False)
        items = Order.order_item_set.all()
    else:
        items = []
        Order = {'get_cart_total': 0, 'get_cart_items': 0}
    context = {'items': items, 'order': Order}
    return render(request,'store/checkout.html',context)