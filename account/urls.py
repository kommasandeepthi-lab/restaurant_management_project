from django.urls import path, include
from django.conf.urls.static import static
from django conf import settings
from . import views
from .views import contact_view, contact_success_view
urlpatterns = [
    path('', include('your_app_name.urls')),
    path('', views.homepage, name='homepage'),
    path("about/", views.about_view, name="about"),
    path("contact/", contact_view, name="contact"),
    path("contact/success/", contact_success_view, name="contact_success"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)