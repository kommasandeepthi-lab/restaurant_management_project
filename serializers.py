from rest_framework import serializers
from .models import MenuItem

class MenuItemSerializer(serializers.ModdelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'description', 'price', 'image', 'is_available']