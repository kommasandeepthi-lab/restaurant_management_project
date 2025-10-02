from rest_framework import serializer
from .models import Restaurant

class RestaurantHoursSerializer(serializers.ModelSerializer):
    opening_hours = serializer.SerializerMethodField()

    class Meta:
        model = Restaurant
        fields = ["opening_hours"]

    def get_opening_hours(self, obj):
        return f"{obj.opening_time.strftime('%I:%M %p')} - {obj.closing_time.strftime('%I:%M %p)} ({obj.timezone})"