from rest_framework import serializers
from .models import MenuItem

class DailySpecialSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'description', 'price']