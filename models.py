from django.db import models
from django.utils import timezone
from datetime import timedelta

class Reservation(models.Model):
    customer_name = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"Reservation for {self.customer_name} from {self.start_time} to {self.end_time}"

    @classmethod
    def get_available_slots(cls, start_range, end_range, slot_length=60):
        existing_reservatioms = cls.objects.filter(
            start_time__lt=end_range,
            end_time__gt=start_range
        ).order_by('start_time')

        available_slots = []
        current_start = start_range

        while current_start + timedelta(minutes=slot_length) <= end_range:
            slot_end = current_start + timedelta(minutes=slot_length)

            overlap = existing_reservatioms.filter(
                start_time__lt=slot_end,
                end_time__gt=current_start
            ).exists()

            if not overlap:
                available_slots.append((current_start, slot_end))

            current_start = slot_end

        return available_slots