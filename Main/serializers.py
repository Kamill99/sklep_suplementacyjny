from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Supplement, Ocena


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']
        extra_kwargs = {'password': {'required': True, 'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class OcenySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ocena
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.opinia = validated_data.get('opinia', instance.opinia)
        instance.nota = validated_data.get('nota', instance.nota)
        instance.save()

        return instance


class SupplementSerializer(serializers.ModelSerializer):
    oceny = OcenySerializer(many=True)

    class Meta:
        model = Supplement
        fields = ['nazwa', 'opis', 'dostepnosc', 'cena', 'rodzaj_suplementu', 'pojemnosc_suplementu', 'oceny']
        read_only_fields = ['oceny']
