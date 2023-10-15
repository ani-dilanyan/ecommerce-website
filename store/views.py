from django.shortcuts import render
from .models import *

# Create your views here.
def store(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/store.html', context)

def get_cart_objects(req):
    if req.user.is_authenticated:
        customer = req.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    context = {'items': items, 'order': order}
    return context

def cart(request):
    context = get_cart_objects(request)
    return render(request, 'store/cart.html', context)


def checkout(request):
    context = get_cart_objects(request)
    return render(request, 'store/checkout.html', context)
