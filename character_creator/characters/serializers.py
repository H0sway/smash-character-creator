# Import modules, models
from rest_framework import serializers
from characters.models import .

class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Character
        fields = '__all__'

class NeutralAttackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Neutral_Attack
        fields = '__all__'

class ForwardTiltSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Forward_Tilt
        fields = '__all__'

class UpTiltSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Up_Tilt
        fields = '__all__'

class DownTiltSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Down_Tilt
        fields = '__all__'

class ForwardSmashSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Forward_Smash
        fields = '__all__'

class UpSmashSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Up_Smash
        fields = '__all__'

class DownSmashSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Down_Smash
        fields = '__all__'

class DashAttackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dash_Attack
        fields = '__all__'

class ForwardArialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Forward_Arial
        fields = '__all__'

class BackwardArialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Backward_Arial
        fields = '__all__'

class UpArialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Up_Arial
        fields = '__all__'

class DownArialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Down_Arial
        fields = '__all__'

class ForwardThrowSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Forward_Throw
        fields = '__all__'

class BackwardThrowSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Backward_Throw
        fields = '__all__'

class UpThrowSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Up_Throw
        fields = '__all__'

class DownThrowSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Down_Throw
        fields = '__all__'

class NeutralSpecialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Neutral_Special
        fields = '__all__'

class SideSpecialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Side_Special
        fields = '__all__'

class UpSpecialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Up_Special
        fields = '__all__'

class DownSpecialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Down_Special
        fields = '__all__'

class FinalSmashSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Final_Smash
        fields = '__all__'
