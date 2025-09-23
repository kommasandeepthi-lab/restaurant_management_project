from rest_framework import serializers
from.models import Order

class OrderStatusUpdateSerializer(serializer.Serializer):
    order_id = serializers.IntegerField()
    new_status = serializers.ChoiceField(choices=Order.STATUS_CHOICES)