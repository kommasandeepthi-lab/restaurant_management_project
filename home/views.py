from django.shortcuts import render
import requests
from django.conf import settings
from .models import OpeningHour, TodaySpecial
from datetime import datetime
from .models import MenuItem
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

def about(request):
    return render(request, "about.html")

def reservations(request):
    return render(request, "reservations.html")

def home(request):
    context = {
        "year": datetime.now().year
    }
    return render(request, "home.html", context)

def our_story_view(request):
    return render(request, "our_story.html")

def menu_view(request):
    query = request.GET.get("q")
    if query:
        menu_items = MenuItem.objects.filter(name__icontains=query)
    else:
        menu_items = MenuItem.objects.all()

return render(request, "menu.html", {"menu_items": menu_items, "query": query})