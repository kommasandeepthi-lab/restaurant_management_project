from rest_framework import serializers
from .models import UserReview

class UserReviewSerializer(serializer.ModelSerializer):
    class Meta:
        model = UserReview
        fields = ['id', 'user', 'menu_item' 'rating', 'comment', 'created_at']
        read_only_fields = ['id', 'created_at']

    def validate_rating(self, value):
        if not(1 <= value <= 5):
            raise serializer.ValidationError("Rating must be between 1 and 5.")
        return value