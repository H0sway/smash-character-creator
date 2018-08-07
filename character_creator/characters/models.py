# Import modules
import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=50)
    series = models.CharField(max_length=50)
    description = models.CharField(max_length=2000)
    neutral_attack = models.ForeignKey(Neutral_Attack, on_delete=models.CASCADE)
    forward_tilt = models.ForeignKey(Forward_Tilt, on_delete=models.CASCADE)
    up_tilt = models.ForeignKey(Up_Tilt, on_delete=models.CASCADE)
    down_tilt = models.ForeignKey(Down_Tilt, on_delete=models.CASCADE)
    forward_smash = models.ForeignKey(Forward_Smash, on_delete=models.CASCADE)
    up_smash = models.ForeignKey(Up_Smash, on_delete=models.CASCADE)
    down_smash = models.ForeignKey(Down_Smash, on_delete=models.CASCADE)
    dash_attack = models.ForeignKey(Dash_Attack, on_delete=models.CASCADE)
    neutral_arial = models.ForeignKey(Neutral_Arial, on_delete=models.CASCADE)
    forward_arial = models.ForeignKey(Forward_Arial, on_delete=models.CASCADE)
    backward_arial = models.ForeignKey(Backward_Arial, on_delete=models.CASCADE)
    up_arial = models.ForeignKey(Up_Arial, on_delete=models.CASCADE)
    down_arial = models.ForeignKey(Down_Arial, on_delete=models.CASCADE)
    forward_throw = models.ForeignKey(Forward_Throw, on_delete=models.CASCADE)
    backward_throw = models.ForeignKey(Backward_Throw, on_delete=models.CASCADE)
    up_throw = models.ForeignKey(Up_Throw, on_delete=models.CASCADE)
    down_throw = models.ForeignKey(Down_Throw, on_delete=models.CASCADE)
    neutral_special = models.ForeignKey(Neutral_Special, on_delete=models.CASCADE)
    forward_special = models.ForeignKey(Forward_Special, on_delete=models.CASCADE)
    up_special = models.ForeignKey(Up_Special, on_delete=models.CASCADE)
    down_special = models.ForeignKey(Down_Special, on_delete=models.CASCADE)
    final_smash = models.ForeignKey(Final_Smash, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)

class Neutral_Attack(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    attack_name = models.CharField(max_length=50)
    attack_description = models.Charfield(max_length=1000)
    image = models.ImageField(default="default.png")

class Forward_Tilt(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    attack_name = models.CharField(max_length=50)
    attack_description = models.Charfield(max_length=1000)
    image = models.ImageField(default="default.png")

class Up_Tilt(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    attack_name = models.CharField(max_length=50)
    attack_description = models.Charfield(max_length=1000)
    image = models.ImageField(default="default.png")

class Down_Tilt(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    attack_name = models.CharField(max_length=50)
    attack_description = models.Charfield(max_length=1000)
    image = models.ImageField(default="default.png")

class Forward_Smash(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    attack_name = models.CharField(max_length=50)
    attack_description = models.Charfield(max_length=1000)
    image = models.ImageField(default="default.png")

class Up_Smash(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    attack_name = models.CharField(max_length=50)
    attack_description = models.Charfield(max_length=1000)
    image = models.ImageField(default="default.png")

class Down_Smash(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    attack_name = models.CharField(max_length=50)
    attack_description = models.Charfield(max_length=1000)
    image = models.ImageField(default="default.png")

class Dash_Attack(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    attack_name = models.CharField(max_length=50)
    attack_description = models.Charfield(max_length=1000)
    image = models.ImageField(default="default.png")

class Neutral_Arial(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    attack_name = models.CharField(max_length=50)
    attack_description = models.Charfield(max_length=1000)
    image = models.ImageField(default="default.png")

class Forward_Arial(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    attack_name = models.CharField(max_length=50)
    attack_description = models.Charfield(max_length=1000)
    image = models.ImageField(default="default.png")

class Backward_Arial(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    attack_name = models.CharField(max_length=50)
    attack_description = models.Charfield(max_length=1000)
    image = models.ImageField(default="default.png")

class Up_Arial(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    attack_name = models.CharField(max_length=50)
    attack_description = models.Charfield(max_length=1000)
    image = models.ImageField(default="default.png")

class Down_Arial(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    attack_name = models.CharField(max_length=50)
    attack_description = models.Charfield(max_length=1000)
    image = models.ImageField(default="default.png")

class Forward_Throw(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    attack_name = models.CharField(max_length=50)
    attack_description = models.Charfield(max_length=1000)
    image = models.ImageField(default="default.png")

class Backward_Throw(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    attack_name = models.CharField(max_length=50)
    attack_description = models.Charfield(max_length=1000)
    image = models.ImageField(default="default.png")

class Up_Throw(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    attack_name = models.CharField(max_length=50)
    attack_description = models.Charfield(max_length=1000)
    image = models.ImageField(default="default.png")

class Down_Throw(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    attack_name = models.CharField(max_length=50)
    attack_description = models.Charfield(max_length=1000)
    image = models.ImageField(default="default.png")

class Neutral_Special(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    attack_name = models.CharField(max_length=50)
    attack_description = models.Charfield(max_length=1000)
    image = models.ImageField(default="default.png")

class Side_Special(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    attack_name = models.CharField(max_length=50)
    attack_description = models.Charfield(max_length=1000)
    image = models.ImageField(default="default.png")

class Up_Special(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    attack_name = models.CharField(max_length=50)
    attack_description = models.Charfield(max_length=1000)
    image = models.ImageField(default="default.png")

class Down_Special(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    attack_name = models.CharField(max_length=50)
    attack_description = models.Charfield(max_length=1000)
    image = models.ImageField(default="default.png")

class Final_Smash(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    attack_name = models.CharField(max_length=50)
    attack_description = models.Charfield(max_length=1000)
    image = models.ImageField(default="default.png")
