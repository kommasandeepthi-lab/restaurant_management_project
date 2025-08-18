from django.shortcuts import render
import requests
from django.conf import settings
from .models import OpeningHour, TodaySpecial
# Create your views here.

def home_view(request):
    context = {
        'restaurant_name': 'The Tasty Table',
        'phone_number': settings.RESTAURANT_PHONE
    }
    return render(request, 'home.html', context)
    
    api_url = 'http://localhost:8000/api/menu/'
    try:
        response = requests.get(api_url)
        menu_items = response.json()
    except Exception as e:
        menu_items = []
    return render(request, 'home.html', {'menu_items': menu_items})

def homepage(request):
    specials = TodaySpecial.objects.all()
    hours = OpeningHour.objects.all()
    return render(request, 'home.html', {'specials': specials, 'hours': hours})