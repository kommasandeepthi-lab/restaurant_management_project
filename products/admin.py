from django.contrib import admin
from .models import *


# Custom Admins
class ItemAdmin(admin.ModelAdmin):
    list_display = ['item_name','item_price','created_at']


# Register your models here.
admin.site.register(Item,ItemAdmin)

restaurant.opening_hours = {
    "Monday": "9:00 AM - 10:00 PM",
    "Tuesday": "9:00 AM - 10:00 PM",
    "Wednesday": "9:00 AM - 10:00 PM",
    "Thursday": "9:00 AM - 10:00 PM",
    "Friday": "9:00 AM - 10:00 PM",
    "Saturday": "9:00 AM - 10:00 PM",
    "Sunday": "Closed"
}
restaurant.save()