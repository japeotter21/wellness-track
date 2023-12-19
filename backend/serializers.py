from rest_framework import serializers
from .models import Caffeine, Exercise, Sleep

class CaffeineSerializer(serializers.Serializer):
    class Meta:
        model = Caffeine
        fields = ('__all__')