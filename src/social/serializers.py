from rest_framework import serializers
from .models import Review


MIN_RATING_VALUE: int = 0
MAX_RATING_VALUE: int = 5


class ReviewSerializer(serializers.ModelSerializer):
    def validate(self, data):
        if data['rating'] > MAX_RATING_VALUE or data['rating'] < MIN_RATING_VALUE:
            raise serializers.ValidationError({'rating': 'rating must in range 0-5'})
        return data

    class Meta:
        model = Review
        fields = '__all__'
