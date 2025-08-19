from django.urls import path, include
from django.conf.urls.static import static
from django conf import settings
from . import views

urlpatterns = [
    path('', include('your_app_name.urls')),
    path('', views.homepage, name='homepage'),
    path("about/", views.about_view, name="about"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)