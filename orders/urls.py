from django.urls import path
from .views import MenuAPIView

urlpatterns = [
    path('api/menu/', MenuAPIViews.as_view(), name='menu-api'),
]