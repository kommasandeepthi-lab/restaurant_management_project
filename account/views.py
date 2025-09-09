from django.shortcuts import render, redirect
from .models import Chef
from django.conf import settings
from .models import Restaurant
from .models import RestaurantInfo
from .forms import SubscriptionForm
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
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

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data("name")
            user_email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            hardcoded_recipent = ""

            subject = "We received your message"
            body = (

            )

            send_mail(
                subject=subject,
                message=body,
                from_email=getattr(settings,""),
                receipient_list=[hardcoded_recipent],
                fail_silently=False,
            )
            
            return redirect("contact_success")
        else:
            form = ContactForm()

        return render(request, "contact.html", {"form": form})

def contact_success_view(request):
    return render(request, "contact_success.html")

def privacy_policy(request):
    return render(request, "privacy_policy.html")

def index(request):
    address = RestaurantInfo.objects.first()
    return render(request, "home.html", {"address": address})

def location(request):
    return render(request, "location.html")

def cart_view(request):
    """
    Simple shopping cart view.
    For now, it just displays a placeholder.
    Later, you can fetch items from session or DB.
    """
    cart_items = request.session.get("cart", [])
    return render(request, "cart/cart.html", {"cart_items": cart_items})

def contact_success_view(request):
    return render(request, "home/contact_success.html")

def place_order(request):
    return redirect("thank_you")

def thank_you(request):
    return render(request, "thank_you.html")

def sitemap_view(request):
    """
    Render a simple sitemap page showing all URL names and links.
    """
    url_patterns = get_resolver().reverse_dict.keys()
    url_list = [url for url in url_patterns if isinstance(url, str)]

    return render(request, "sitemap.html", {"url_list": url_list})

def careers(request):
    return render(request, "careers.html")

    