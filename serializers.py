from rest_framework import serializers
from .models import Review

class ReviewSerializers(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Review
        fields = ['user_name', 'rating', 'comment']