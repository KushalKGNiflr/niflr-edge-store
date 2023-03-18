from rest_framework import serializers
from .models import *

class WeightSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WeightChanges
        fields = '__all__'

class MachineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Machines
        fields = '__all__'

class StoreSessionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StoreSessions
        fields = '__all__'

class StoreModeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StoreModeChange
        fields = '__all__'