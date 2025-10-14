from django.urls import path, include
from django.conf.urls.static import static
from django conf import settings
from . import views      
from .views import contact_view, contact_success_view
from django.shortcuts import render
from .views import MenuItemSearchView
from .views import OrderDetailView
from .views import cancel_order
from .views import get_order_status
from .views import UpdateMenuItemAvailabilityView
from .views import RestaurantInfoView
from .views import MenuCategoryListView
from .views import CreateUserReviewView
from .views import search_menu_items
from .views import RestaurantReviewListView
from .views import OrderStatusView
from .views import OpeningHourListView
from .views import CouponValidationView
from .views import AvailableTablesAPIView, TableDetailAPIView
from .views import MenuItemPriceRangeView
from .views import MenuItemListView
from .views import RestaurantHoursView
from .views import ReviewListView
from .views import UpdateMenuItemAvailabilityView
from .views import FAQListView
from .views import AvailableMenuItemsView
from .views import OrderStatusUpdateView
from home.views import AvailableMenuItemCountView
from .views import OrderSummaryView
from .views import ReviewListView
from .views import CuisineLsitView

urlpatterns = [
    path('', include('your_app_name.urls')),
    path('', views.homepage, name='homepage'),
    path("about/", views.about_view, name="about"),
    path("contact/", contact_view, name="contact"),
    path("contact/success/", contact_success_view, name="contact_success"),
    path("privacy_policy/", views.privacy_policy, name="privacy_policy"),
    path("gallery/", gallery_view, name="gallery"),
    path('location/', views.location_view, name='location'),
    path("contact/", views.contact_view, name="contact"),
    path("contact/success/", views.contact_success_view, name="contact_success"),
    path('menu/', views.menu_view, name="menu"),
    path('reservation', views.reservation_view, name='reservation'),
    path('order', views.order_view, name='order'),
    path("cart/", views.cart_view, name="cart"),
    path("reservations/", views.reservations, name="reservations"),
    path("sitemap.xml", views.sitemap, name="sitemap"),
    path("", views.home, name="home"),
    path("", views.home_view, name="home"),
    path('menu-categories/', MenuCategoryListView.as_view(), name='menu-category-list'),
    path('items-by-category/', MenuItemsByCategoryView.as_view(), name='items-by-category'),
    path('items/search/', MenuItemSearchView.as_view(), name='menu-item-search'),
    path("<str:order_id>/", OrderDetailView(), name="order-detail"),
    path("cancel/<int:order_id/", cancel_order, name="cancel-order"),
    path("orders/<int:order_id>/status/", get_order_status, name="order-status"),
    path('menu/<int:pk>/availability/', UpdateMenuItemAvailabilityView.as_view(), name='update-menu-availability'),
    path('restaurant/info/', RestaurantInfoView.as_view(), name='restaurant-info'),
    path('menu/categories/', MenuCategoryListView.as_view(), name='menu-categories'),
    path('api/reviews/', CreateUserReviewView.as_view(), name='create-review'),
    path('menu/search/', search_menu_items, name='menu-search'),
    path(
        "restaurants/<int:restaurant_id>/reviews/",
        RestaurantReviewListView.as_view(),
        name="restaurant-reviews",
    ),
    path("orders/<str:unique_id>/status/", OrderStatusView.as_view(), name="order-status"),
    path("opening-hours/", OpeningHourListView.as_view(), name="opening-hours"),
    path("coupon/validate/", CouponValidationView.as_view, name="coupon-validate"),
    path('api/tables/available/', AvailableTablesAPIView.as_view(), name='available-tables-api'),
    path('api/tables/<int:pk>/', TableDetailAPIView.as_view(), name='table-detail-api'),
    path("menu-items/price-range/", MenuItemPriceRangeView.as_view(), name="menu-items-price-range"),
    path("menu-items/", MenuItemListView.as_view(), name="menu-items-list"),
    path("restaurant/hours/", RestaurantHoursView.as_view(), name="restaurant-hours")
    path("api/reviews/", ReviewListView.as_view(), name="review-list"),
    path("api/menu-items/<int:pk>/availability/", MenuItemAvailabilityView.as_view(), name="menu-item-availability"),
    path('faqs/', FAQListView.as_view(), name='faq-list'),
    path('menu-items/', AvailableMenuItemsView(), name='available-menu-items'),
    path('orders/<int:pk>/update-status/', OrderStatusUpdateView.as_view(), name='update-order-status'),
    path('menu-items/count/', AvailableMenuItemCountView.as_view(), name='available-menu-item-count'),
    path('orders/<int:order_id>/summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('reviews/', ReviewListView.as_view(), name='review-list'),
    path('api/cuisines/', CuisineLsitView.as_view(), name='cuisine-list')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

def custom_permission_denied_view(request, exception=None):
    return render(request, "403.html", status=403)

handler403 = custom_permission_denied_view

def gallery_view(request):
    return render(request, "gallery.html")