from django.shortcuts import render
import requests
from django.conf import settings
# Create your views here.

def home_view(request):
    context = {
        'restaurant_name': 'My Restaurant',
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
