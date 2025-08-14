from django.contrib import admin
from django.urls import path, include

from .views import MenuAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/menu/', include('orders.urls')),
    path('faq/', views.faq_page, name='faq'),
    path('order/', views.order_page, name='order'),
]