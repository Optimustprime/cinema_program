from rest_framework import serializers
from .models import Movie
from django.utils import timezone


class MovieSerializer(serializers.ModelSerializer):
    """serializer for Movies"""

    def validate_start_date(self, value):
        """Validate that the start date is not in the past"""
        if value < timezone.now():
            raise serializers.ValidationError("Start date cannot be in the past")
        return value

    class Meta:
        model = Movie
        fields = ('id', 'name', 'protagonists', 'poster', 'start_date', 'status', 'ranking')
