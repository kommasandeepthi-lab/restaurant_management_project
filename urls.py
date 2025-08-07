from django.urls import path
from .views import reservations_view

urlpatterns = [
    path('reservations/', reservations_view, name='reservations'),
]