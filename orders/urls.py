from django.contrib import admin
from django.urls import path, include

from .views import MenuAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/menu/', include('orders.urls')),
]