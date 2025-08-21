from django.urls import path
from .views import home_view
from . import views

urlpatterns = [
    path('', home_view, name='home'),
    path('', views.homepage, name='home'),
    path("menu/", views.menu_view, name="menu"),
    path("about/", views.about, name="about"),
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("reservations/", views.reservations, name="reservations"),
]