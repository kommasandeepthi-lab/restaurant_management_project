from django.urls import path
from .views import menu_list_view

urlpatterns = [
    path('menu/', menu_list_view, name='menu_list'),
]