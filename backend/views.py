from django.shortcuts import render
from rest_framework import permissions, viewsets
from .serializers import CaffeineSerializer, ExerciseSerializer, SleepSerializer
from .models import Caffeine, Exercise, Sleep

# Create your views here.

class CaffeineViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Caffeine.objects.all()
    serializer_class = CaffeineSerializer
    permission_classes = [permissions.IsAuthenticated]

class ExerciseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = [permissions.IsAuthenticated]

class SleepViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Sleep.objects.all()
    serializer_class = SleepSerializer
    permission_classes = [permissions.IsAuthenticated]