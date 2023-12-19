from django.shortcuts import render
from rest_framework import generics
from .serializers import CaffeineSerializer
from .models import Caffeine

# Create your views here.

class CaffeineView(generics.CreateAPIView):
    queryset = Caffeine.objects.all()
    serializer_class = CaffeineSerializer