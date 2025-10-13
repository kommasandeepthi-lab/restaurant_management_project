from django.contrib import admin
from .models import Table
from .models import MenuCategory

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('table_number', 'capacity', 'is_available', 'location')
    search_fields = ('table_number', 'location')
    list_filter = ('is_available', 'location')