from .models import Table

def get_available_tables_by_capacity(num_guests):
    return Table.objects.filter(is_available=True, capacity__gte=num_guests)