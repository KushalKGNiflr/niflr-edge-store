from rest_framework import serializers
from .models import *

class TicketSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tickets
        fields = '__all__'