from django.db .models import Sum
from .models import Order

def get_daily_total(data):

    result = Order.objects.filter(created_at__date=date).aggregate(total_sum=Sum('total_price'))
    return result['total_sum'] or 0