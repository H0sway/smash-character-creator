# Import modules, models
from rest_framework import serializers
from characters import models

class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Character
        fields = '__all__'

class NeutralAttackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Neutral_Attack
        fields = '__all__'

class ForwardTiltSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Forward_Tilt
        fields = '__all__'

class UpTiltSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Up_Tilt
        fields = '__all__'

class DownTiltSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Down_Tilt
        fields = '__all__'

class ForwardSmashSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Forward_Smash
        fields = '__all__'

class UpSmashSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Up_Smash
        fields = '__all__'

class DownSmashSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Down_Smash
        fields = '__all__'

class DashAttackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Dash_Attack
        fields = '__all__'

class ForwardArialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Forward_Arial
        fields = '__all__'

class BackwardArialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Backward_Arial
        fields = '__all__'

class UpArialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Up_Arial
        fields = '__all__'

class DownArialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Down_Arial
        fields = '__all__'

class ForwardThrowSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Forward_Throw
        fields = '__all__'

class BackwardThrowSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Backward_Throw
        fields = '__all__'

class UpThrowSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Up_Throw
        fields = '__all__'

class DownThrowSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Down_Throw
        fields = '__all__'

class NeutralSpecialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Neutral_Special
        fields = '__all__'

class SideSpecialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Side_Special
        fields = '__all__'

class UpSpecialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Up_Special
        fields = '__all__'

class DownSpecialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Down_Special
        fields = '__all__'

class FinalSmashSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Final_Smash
        fields = '__all__'
