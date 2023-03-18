from rest_framework import serializers
from .models import *

class UserSessionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserSessions
        fields = '__all__'

class UserCycleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserCycle
        fields = '__all__'

class UserDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserDetails
        fields = '__all__'

class CartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Carts
        fields = '__all__'