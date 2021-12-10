from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Supplement


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class SupplementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplement
        fields = ['name', 'description', 'available']
