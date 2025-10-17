from django.contrib import admin
from .models import Table
from .models import MenuCategory
from .models import Restaurant
from home.models import DailyOperatingHours

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('table_number', 'capacity', 'is_available', 'location')
    search_fields = ('table_number', 'location')
    list_filter = ('is_available', 'location')

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(DailyOperatingHours)