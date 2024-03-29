from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from .serializers import CaffeineSerializer, WaterSerializer, AlcoholSerializer, ExerciseSerializer, SleepSerializer, MoodSerializer, FocusSerializer, ScreenTimeSerializer
from .models import Caffeine, Water, Alcohol, Exercise, Sleep, Mood, Focus, ScreenTime

# Create your views here.

class CaffeineViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Caffeine.objects.all()
    serializer_class = CaffeineSerializer

class WaterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Water.objects.all()
    serializer_class = WaterSerializer

class AlcoholViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Alcohol.objects.all()
    serializer_class = AlcoholSerializer

class ExerciseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

class SleepViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Sleep.objects.all()
    serializer_class = SleepSerializer

class MoodViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Mood.objects.all()
    serializer_class = MoodSerializer
    
class FocusViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Focus.objects.all()
    serializer_class = FocusSerializer
    
class ScreenTimeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ScreenTime.objects.all()
    serializer_class = ScreenTimeSerializer