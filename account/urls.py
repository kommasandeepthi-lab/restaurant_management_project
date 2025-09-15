from django.urls import path, include
from django.conf.urls.static import static
from django conf import settings
from . import views
from .views import contact_view, contact_success_view
from django.shortcuts import render

urlpatterns = [
    path('', include('your_app_name.urls')),
    path('', views.homepage, name='homepage'),
    path("about/", views.about_view, name="about"),
    path("contact/", contact_view, name="contact"),
    path("contact/success/", contact_success_view, name="contact_success"),
    path("privacy_policy/", views.privacy_policy, name="privacy_policy"),
    path("gallery/", gallery_view, name="gallery"),
    path('location/', views.location_view, name='location'),
    path("contact/", views.contact_view, name="contact"),
    path("contact/success/", views.contact_success_view, name="contact_success"),
    path('menu/', views.menu_view, name="menu"),
    path('reservation', views.reservation_view, name='reservation'),
    path('order', views.order_view, name='order'),
    path("cart/", views.cart_view, name="cart"),
    path("reservations/", views.reservations, name="reservations"),
    path("sitemap.xml", views.sitemap, name="sitemap"),
    path("", views.home, name="home"),
    path("", views.home_view, name="home"),
    path('menu-categories/', MenuCategoryListView.as_view(), name='menu-category-list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

def custom_permission_denied_view(request, exception=None):
    return render(request, "403.html", status=403)

handler403 = custom_permission_denied_view

def gallery_view(request):
    return render(request, "gallery.html")