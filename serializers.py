from rest_framework import serializers
from .models import UserReview

class UserReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserReview
        fields = ['id', 'menu_item', 'rating', 'comment', 'created_at']
        read_only_fields = ['id', 'created_at']