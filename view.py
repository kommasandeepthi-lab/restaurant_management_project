from .models import RestaurantInfo

def home(request):
    restaurant_info = RestaurantInfo.objects.first()
    restaurant_name = restaurant_info.name if restaurant_info else "Our Restaurant"

    return render(request, 'home.html', {
        'restaurant_name': restaurant_name
    })