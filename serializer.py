from rest_framework import serializer
from .models import Order
from home.models import MenuItem

class MenuItemSerializer(serializer.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ["id", "name", "price"]

class OrderSerializer(serializer.ModelSerializer):
    items = MenuItemSerializer(many=True, read_only=True)
    user = serializer.StringRelatedField()

    class Meta:
        model = Order
        fields = ["order_id", "user", "items", "total_price", "created_at"]