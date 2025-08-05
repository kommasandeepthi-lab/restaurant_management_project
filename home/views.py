from django.shortcuts import render
import requests
# Create your views here.

def home(request):
    api_url = 'http://localhost:8000/api/menu/'
    try:
        response = requests.get(api_url)
        menu_items = response.json()
    except Exception as e:
        menu_items = []
    return render(request, 'home.html', {'menu_items': menu_items})
