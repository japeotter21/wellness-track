from rest_framework import serializers
from .models import Caffeine, Water, Exercise, Sleep, Alcohol, Mood, Focus, ScreenTime

class CaffeineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caffeine
        fields = ('__all__')

class WaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Water
        fields = ('__all__')
        
class AlcoholSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alcohol
        fields = ('__all__')

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ('__all__')

class SleepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sleep
        fields = ('__all__')
        
class MoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mood
        fields = ('__all__')

class FocusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Focus
        fields = ('__all__')

class ScreenTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScreenTime
        fields = ('__all__')