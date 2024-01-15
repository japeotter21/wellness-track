from rest_framework import serializers
from .models import Caffeine, Exercise, Sleep

class CaffeineSerializer(serializers.Serializer):
    class Meta:
        model = Caffeine
        fields = ('__all__')

class ExerciseSerializer(serializers.Serializer):
    class Meta:
        model = Exercise
        fields = ('__all__')

class SleepSerializer(serializers.Serializer):
    class Meta:
        model = Sleep
        fields = ('__all__')