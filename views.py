from django.shortcuts import rneder

def home-page(request):
    breadcrumbs = [
        ("Home", "/")
    ]
    return render(request, 'home.html', {'breadcrumbs': breadcrumbs, 'restaurant_name': 'My Restaurant'})

def faq_page(request):
    breadcrumbs = [
        ("Home", "/"),
        ("FAQ", "")
    ]
    return render(request, 'faq.html', {'breadcrumbs': breadcrumbs})

def order_page(request):
    breadcrumbs = [
        ("Home", "/"),
        ("Order Now", "")
    ]
    return render(request, 'order.html', {'breadcrumbs': breadcrumbs})