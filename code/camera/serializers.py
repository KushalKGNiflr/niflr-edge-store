from rest_framework import serializers
from .models import *

class VideoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Videos
        fields = '__all__'

class CameraSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cameras
        fields = '__all__'

class ScannerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Scanners
        fields = '__all__'