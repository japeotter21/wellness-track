from rest_framework import serializers
from .models import Caffeine, Water, Exercise, Sleep

class CaffeineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caffeine
        fields = ('__all__')

class WaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Water
        fields = ('__all__')

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ('__all__')

class SleepSerializer(serializers.ModelSerializer):
    awake = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")
    
    class Meta:
        model = Sleep
        fields = ('__all__')