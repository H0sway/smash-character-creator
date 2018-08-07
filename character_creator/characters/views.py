from django.shortcuts import render
from characters import models
from characters import serializers
from rest_framework import generics
# Create your views here.

class CharacterListCreate(generics.ListCreateAPIView):
    queryset = models.Character.objects.all()
    serializer_class = serializers.CharacterSerializer

class MovesetListCreate(generics.ListCreateAPIView):
    queryset = models.Moveset.objects.all()
    serializer_class = serializers.MovesetSerializer
