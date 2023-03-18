from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets, permissions

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Videos.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [permissions.IsAuthenticated]

class CameraViewSet(viewsets.ModelViewSet):
    queryset = Cameras.objects.all()
    serializer_class = CameraSerializer
    permission_classes = [permissions.IsAuthenticated]

class ScannerViewSet(viewsets.ModelViewSet):
    queryset = Scanners.objects.all()
    serializer_class = ScannerSerializer
    permission_classes = [permissions.IsAuthenticated]
