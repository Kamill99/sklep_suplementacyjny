from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Supplement, Ocena


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


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
