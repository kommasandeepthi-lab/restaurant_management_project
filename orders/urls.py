from django.urls import path
from .views import MenuAPIView

urlpatterns = [
    path('api/menu/', MenuAPIView.as_view(), name='menu-api'),
]