from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, render
from .models import     Product, Order, OrderItem, Customer
from django.http import JsonResponse
import json
# Create your views here.



def home(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cart_items = order.all_total_item
    else:
        items = []
        order = {'all_total_cost':0, 'all_total_item':0}
        cart_items = order['all_total_item']

    
    search_product = request.GET.get('search_product')
    search_mode = False
    if search_product:
        products = Product.objects.filter(name__icontains=search_product)
        search_mode = True
    else:
        products = Product.objects.all()
    
    return render(request, 'App/index.html', {'products': products, 'search_mode': search_mode, 'cart_items': cart_items})


def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        order_items = order.orderitem_set.all()

        total_cost = order.all_total_cost
        total_item = order.all_total_item

    else:
        order_items = []
        total_cost = 0
        total_item = 0

    context = {'order_items':order_items , 'total_cost':total_cost, 'total_item':total_item}   
    return render(request,"App/cart.html",context)

def checkout(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        order_items = order.orderitem_set.all()

        total_cost = order.all_total_cost
        total_item = order.all_total_item

    else:  
        order_items = []
        total_cost = 0
        total_item = 0
        
    context = {'order_items':order_items , 'total_cost':total_cost, 'total_item':total_item}

    return render(request,"App/checkout.html", context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productID']  
    action = data['action']

    print('Action:', action)
    print('Product ID:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity += 1
    elif action == 'remove':    
        orderItem.quantity -= 1
    elif action == 'fav':
        product.favorite = True
        product.save()
    elif action == 'delete':
        orderItem.quantity = 0

    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()
    
    return JsonResponse('Item was added', safe=False)
    

def favorite(request):

    if request.user.is_authenticated:
        products = Product.objects.filter(favorite=True)

    context = {'fav_products':products}
    return render(request,"App/favorites.html",context)