from django.shortcuts import render
import random

def order_confirmation(request):
    order_number = random.randit(100000, 999999)
    return render(request, 'order_confirmation.html', {'order_number': order_number})