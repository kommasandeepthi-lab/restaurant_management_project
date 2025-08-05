from django.urls import path
from .views import MenuAPIViews

urlpatterns = [
    path('api/menu/', MenuAPIViews.as_view(), name='menu-api'),
    ]