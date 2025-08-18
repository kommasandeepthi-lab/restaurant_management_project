from django.shortcuts import render, redirect, get_object_or_404
from .models import MenuItem
from .utils import get_cart, save_cart

def add_to_cart(request, item_id):
    item = get_object_or_404(MenuItem, id=item_id)
    cart = get_cart(request)

    if str(item_id) in cart:
        cart[str(item_id)]['quantity'] += 1
    else :
        cart[str(item_id)] = {
            'name': item.name,
            'price': str(item.price),
            'quantity': 1
        }

    save_cart(request, cart)
    return redirect('view_cart')

def view_cart(request):
    cart = get_cart(request)
    total = sum(float(item['price']) * item['quantity'] for item in cart.values())
    return render(request, 'cart.html', {'cart': cart, 'total': total})

def remove_from_cart(request, item_id):
    cart = get_cart(request)
    if str(item_id) in cart:
        del cart[str(item_id)]
        save_cart(request, cart)
    return redirect('view_cart')