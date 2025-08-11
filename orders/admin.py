from django.contrib import admin
from .models import Menu, Order
from .models import Restaurant
# Register your models here.

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')
    search_fields = ('name')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'total_amount', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('customer_username',)
    filter_horizontal = ('order_items',)

    admin.site.register(Restaurant)