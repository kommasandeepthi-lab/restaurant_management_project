from django.shortcuts import render
from .models import Restaurant

def homepage(request):
    restaurant = Restaurant.objects.first()
    return render(request, 'index.html', {'restaurant': restaurant})
    
    current_datetime = timezone.now()
    return render(request, 'index.html', {'current_datetime': current_datetime})