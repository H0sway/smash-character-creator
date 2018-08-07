from django.shortcuts import render
from characters import models
from characters import serializers
from rest_framework import generics
# Create your views here.

class CharacterListCreate(generics.ListCreateAPIView):
    queryset = models.Character.objects.all()
    serializer_class = serializers.CharacterSerializer

class NeutralAttackListCreate(generics.ListCreateAPIView):
    queryset = models.Neutral_Attack.objects.all()
    serializer_class = serializers.NeutralAttackSerializer

class ForwardTiltListCreate(generics.ListCreateAPIView):
    queryset = models.Forward_Tilt.objects.all()
    serializer_class = serializers.ForwardTiltSerializer

class UpTiltListCreate(generics.ListCreateAPIView):
    queryset = models.Up_Tilt.objects.all()
    serializer_class = serializers.UpTiltSerializer

class DownTiltListCreate(generics.ListCreateAPIView):
    queryset = models.Down_Tilt.objects.all()
    serializer_class = serializers.DownTiltSerializer

class ForwardSmashListCreate(generics.ListCreateAPIView):
    queryset = models.Forward_Smash.objects.all()
    serializer_class = serializers.ForwardSmashSerializer

class UpSmashListCreate(generics.ListCreateAPIView):
    queryset = models.Up_Smash.objects.all()
    serializer_class = serializers.UpSmashSerializer

class DownSmashListCreate(generics.ListCreateAPIView):
    queryset = models.Down_Smash.objects.all()
    serializer_class = serializers.DownSmashSerializer

class DashAttackListCreate(generics.ListCreateAPIView):
    queryset = models.Dash_Attack.objects.all()
    serializer_class = serializers.DashAttackSerializer

class ForwardArialListCreate(generics.ListCreateAPIView):
    queryset = models.Forward_Arial.objects.all()
    serializer_class = serializers.ForwardArialSerializer

class BackwardArialListCreate(generics.ListCreateAPIView):
    queryset = models.Backward_Arial.objects.all()
    serializer_class = serializers.BackwardArialSerializer

class UpArialListCreate(generics.ListCreateAPIView):
    queryset = models.Up_Arial.objects.all()
    serializer_class = serializers.UpArialSerializer

class DownArialListCreate(generics.ListCreateAPIView):
    queryset = models.Down_Arial.objects.all()
    serializer_class = serializers.DownArialSerializer

class ForwardThrowListCreate(generics.ListCreateAPIView):
    queryset = models.Forward_Throw.objects.all()
    serializer_class = serializers.ForwardThrowSerializer

class BackwardThrowListCreate(generics.ListCreateAPIView):
    queryset = models.Backward_Throw.objects.all()
    serializer_class = serializers.BackwardThrowSerializer

class UpThrowListCreate(generics.ListCreateAPIView):
    queryset = models.Up_Throw.objects.all()
    serializer_class = serializers.UpThrowSerializer

class DownThrowListCreate(generics.ListCreateAPIView):
    queryset = models.Down_Throw.objects.all()
    serializer_class = serializers.DownThrowSerializer

class NeutralSpecialListCreate(generics.ListCreateAPIView):
    queryset = models.Neutral_Special.objects.all()
    serializer_class = serializers.NeutralSpecialSerializer

class SideSpecialListCreate(generics.ListCreateAPIView):
    queryset = models.Side_Special.objects.all()
    serializer_class = serializers.SideSpecialSerializer

class UpSpecialListCreate(generics.ListCreateAPIView):
    queryset = models.Up_Special.objects.all()
    serializer_class = serializers.UpSpecialSerializer

class DownSpecialListCreate(generics.ListCreateAPIView):
    queryset = models.Down_Special.objects.all()
    serializer_class = serializers.DownSpecialSerializer

class FinalSmashListCreate(generics.ListCreateAPIView):
    queryset = models.Final_Smash.objects.all()
    serializer_class = serializers.FinalSmashSerializer
