# Import modules, models
from rest_framework import serializers
from characters import models

class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Character
        fields = '__all__'

class MovesetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Moveset
        fields = '__all__'
