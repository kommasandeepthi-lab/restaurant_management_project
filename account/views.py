from django.shortcuts import render, redirect
from .models import Chef
from django.conf import settings
from .models import Restaurant
from .models import RestaurantInfo
from .forms import SubscriptionForm
# Create your views here.

def homepage_view(request):
    restaurant_name = getattr(settings, 'Restaurant_NAME', 'MY Restaurant')
    return render(request, 'home.html', {'restaurant_name': restaurant.name})

def about_view(request):
    return render(request, 'about.html')

def homepage(request):
    restaurant = Restaurant.objects.first()
    return render(request, 'homepage.html', {'restaurant': restaurant})

def home_page(request):
    breadcrumbs = [("Home", "/")]
    context = {
        'breadcrumbs': breadcrumbs,
        'restaurant_name': 'My Restaurant'
        'restaurant_phone': settings.RESTAURANT_PHONE
    }
    return render(request, 'home.html', context)

def about_view(request):
    restaurant = RestaurantInfo.objects.first()
    return render(request, "about.html", {"restaurant": restaurant})

def about_chef(request):
    chef = Chef.objects.first()
    return render(request, "about_chef.html", {"chef": chef})

def home(request):
    context = {
        "page_title": "Foodie Restaurant"
    }
    return render(request, "home.html", context)

def home(request):
    if request.method == "POST":
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SubscriptionForm()

    return render(request, "home.html, {"form": form})