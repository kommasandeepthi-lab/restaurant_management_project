from datetime import datetime
from django.utils import timezone
from home.models import DailyOperatingHours

def is_restaurant_open():
    now = timezone.localtime()
    current_day = now.strftime("%A")
    current_time = now.time()

    try:
        today_hours = DailyOperatingHours.objects.get(day=current_day)
    except DailyOperatingHours.DoesNotExist:
        return False

    if today_hours.opening_time <= current_time <= today_hours.closing_time:
        return True
    return False