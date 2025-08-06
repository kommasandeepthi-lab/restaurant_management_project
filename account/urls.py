from django.urls import path
from .views import homepage_view, about_view

urlpatterns = [
    path('', homepage_views, name='homepage'),
    path('about/', about_view, name='about'),
]