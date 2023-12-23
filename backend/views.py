from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import CaffeineSerializer
from .models import Caffeine

# Create your views here.

@api_view(['PUT', 'DELETE'])
def CaffeineView(request, pk):
    try:
        Caffeine = Caffeine.objects.get(pk=pk)
    except Caffeine.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = CaffeineSerializer(Caffeine, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        Caffeine.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)