from django.urls import path
from . import views

urlpatterns = [
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('feedback/', views.feedback_view, name='feedback'),
]