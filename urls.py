from django.urls import path
from . import views
from .views import contact_view

urlpatterns = [
    path('', views.home, name='home')
    path('menu/', views.menu, name='menu'),
    path('contact/', contact_view, name='contact'),
]