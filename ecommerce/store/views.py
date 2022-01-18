
from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
# Create your views here.
def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        Order, created = order.objects.get_or_create(customer=customer, complete=False)
        items = Order.order_item_set.all()
        cartItems=Order.get_cart_items
    else:
        items = []
        Order = {'get_cart_total': 0, 'get_cart_items': 0,'shipping':False}
        cartItems=Order['get_cart_items']
    products=product.objects.all()
    context={'products':products,'cartItems':cartItems}
    return render(request,'store/store.html',context)
def cart(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        Order,created=order.objects.get_or_create(customer=customer,complete=False)
        items=Order.order_item_set.all()
        cartItems=Order.get_cart_items
    else:
        items=[]
        Order={'get_cart_total':0,'get_cart_items':0,'shipping':False}
        cartItems=Order['get_cart_items']
    context={'items':items,'order':Order,'cartItems':cartItems}
    return render(request,'store/cart.html',context)
def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        Order, created = order.objects.get_or_create(customer=customer, complete=False)
        items = Order.order_item_set.all()
        cartItems=Order.get_cart_items
    else:
        items = []
        Order = {'get_cart_total': 0, 'get_cart_items': 0,'shipping':False}
    context = {'items': items, 'order': Order,'cartItems':cartItems}
    return render(request,'store/checkout.html',context)
def update_item(request):
    data=json.loads(request.body)
    productId=data['productId']
    action=data['action']
    print('Action:',action)
    print('productId:',productId)
    customer = request.user.customer
    Product=product.objects.get(id=productId)
    Order, created = order.objects.get_or_create(customer=customer, complete=False)
    orderItem,created=order_item.objects.get_or_create(order=Order,product=Product)
    if action=='add':
        orderItem.quantity=(orderItem.quantity + 1)
    elif action=='remove':
        orderItem.quantity = (orderItem.quantity - 1)
    orderItem.save()
    if orderItem.quantity<=0:
        orderItem.delete()
    return JsonResponse('Item was added',safe=False)