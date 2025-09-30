from rest_framework import serializers
from .models import OpeningHour

class OpeningHourSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpeningHour
        fields = ["day", "opening_time", "closing_time"]