from django.urls import path
from .views import home_view
from . import views

urlpatterns = [
    path('', home_view, name='home'),
    path('', views.homepage, name='home'),
    path)"menu/", views.menu_view, name="menu"),
]