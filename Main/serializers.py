from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Suplement


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']
        extra_kwargs = {'password': {'required': True, 'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class SupplementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Suplement
        fields = ['nazwa', 'opis', 'dostepnosc', 'cena', 'rodzaj_suplementu', 'pojemnosc_suplementu']
