from django.urls import path, include
from django.conf.urls.static import static
from django conf import settings

urlpatterns = [
    path('', include('your_app_name.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)