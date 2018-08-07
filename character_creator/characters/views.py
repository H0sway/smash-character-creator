from django.shortcuts import render
from characters.models import .
from leads.serializers import LeadSerializer
from rest_framework import generics
# Create your views here.

class CharacterListCreate(generics.ListCreateAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

class NeutralAttackListCreate(generics.ListCreateAPIView):
    queryset = Neutral_Attack.objects.all()
    serializer_class = NeutralAttackSerializer

class ForwardTiltListCreate(generics.ListCreateAPIView):
    queryset = Forward_Tilt.objects.all()
    serializer_class = ForwardTiltSerializer

class UpTiltListCreate(generics.ListCreateAPIView):
    queryset = Up_Tilt.objects.all()
    serializer_class = UpTiltSerializer

class DownTiltListCreate(generics.ListCreateAPIView):
    queryset = Down_Tilt.objects.all()
    serializer_class = DownTiltSerializer

class ForwardSmashListCreate(generics.ListCreateAPIView):
    queryset = Forward_Smash.objects.all()
    serializer_class = ForwardSmashSerializer

class UpSmashListCreate(generics.ListCreateAPIView):
    queryset = Up_Smash.objects.all()
    serializer_class = UpSmashSerializer

class DownSmashListCreate(generics.ListCreateAPIView):
    queryset = Down_Smash.objects.all()
    serializer_class = DownSmashSerializer

class DashAttackListCreate(generics.ListCreateAPIView):
    queryset = Dash_Attack.objects.all()
    serializer_class = DashAttackSerializer

class ForwardArialListCreate(generics.ListCreateAPIView):
    queryset = Forward_Arial.objects.all()
    serializer_class = ForwardArialSerializer

class BackwardArialListCreate(generics.ListCreateAPIView):
    queryset = Backward_Arial.objects.all()
    serializer_class = BackwardArialSerializer

class UpArialListCreate(generics.ListCreateAPIView):
    queryset = Up_Arial.objects.all()
    serializer_class = UpArialSerializer

class DownArialListCreate(generics.ListCreateAPIView):
    queryset = Down_Arial.objects.all()
    serializer_class = DownArialSerializer

class ForwardThrowListCreate(generics.ListCreateAPIView):
    queryset = Forward_Throw.objects.all()
    serializer_class = ForwardThrowSerializer

class BackwardThrowListCreate(generics.ListCreateAPIView):
    queryset = Backward_Throw.objects.all()
    serializer_class = BackwardThrowSerializer

class UpThrowListCreate(generics.ListCreateAPIView):
    queryset = Up_Throw.objects.all()
    serializer_class = UpThrowSerializer

class DownThrowListCreate(generics.ListCreateAPIView):
    queryset = Down_Throw.objects.all()
    serializer_class = DownThrowSerializer

class SideSpecialListCreate(generics.ListCreateAPIView):
    queryset = Side_Special.objects.all()
    serializer_class = SideSpecialSerializer

class UpSpecialListCreate(generics.ListCreateAPIView):
    queryset = Up_Special.objects.all()
    serializer_class = UpSpecialSerializer

class DownSpecialListCreate(generics.ListCreateAPIView):
    queryset = Down_Special.objects.all()
    serializer_class = DownSpecialSerializer

class FinalSmashListCreate(generics.ListCreateAPIView):
    queryset = Final_Smash.objects.all()
    serializer_class = FinalSmashSerializer
