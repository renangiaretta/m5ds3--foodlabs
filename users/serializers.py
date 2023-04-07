from rest_framework import serializers
from .models import Seasons


class UserSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=10)
    last_name = serializers.CharField(max_length=10)
    email = serializers.EmailField()
    favorite_season = serializers.CharField(
        max_length=30,
        choices=Seasons.choices,
        default=Seasons.DEFAULT
    )

    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()