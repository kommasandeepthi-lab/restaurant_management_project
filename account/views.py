from django.shortcuts import render
from django.conf import settings
from .models import Restaurant
# Create your views here.

def homepage_view(request):
    restaurant_name = getattr(settings, 'Restaurant_NAME', 'MY Restaurant')
    return render(request, 'home.html', {'restaurant_name': restaurant.name})

def about_view(request):
    return render(request, 'about.html')