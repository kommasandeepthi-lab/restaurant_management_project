from django.contrib import admin
from .models import Table
from .models import MenuCategory

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('id', 'table_number', 'capacity', 'is_available')
    search_fields = ('table_number',)
    list_filter = ('is_available',)

admin.site.register(MenuCategory)