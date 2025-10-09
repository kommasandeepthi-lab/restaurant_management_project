from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import MenuCategoryViewSet

router = DefaultRouter()
router.register(r'categories', MenuCategoryViewSet, basename='categories')

urlpatterns = router.urls