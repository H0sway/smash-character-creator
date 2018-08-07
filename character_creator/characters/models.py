# Import modules
import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=50)
    series = models.CharField(max_length=50)
    description = models.CharField(max_length=2000)
    pub_date = models.DateTimeField(auto_now_add=True)

class Neutral_Attack(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    attack_name = models.CharField(max_length=50)
    attack_description = models.CharField(max_length=1000)
    image = models.ImageField(default="default.png")

class Forward_Tilt(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    attack_name = models.CharField(max_length=50)
    attack_description = models.CharField(max_length=1000)
    image = models.ImageField(default="default.png")

class Up_Tilt(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    attack_name = models.CharField(max_length=50)
    attack_description = models.CharField(max_length=1000)
    image = models.ImageField(default="default.png")

class Down_Tilt(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    attack_name = models.CharField(max_length=50)
    attack_description = models.CharField(max_length=1000)
    image = models.ImageField(default="default.png")

class Forward_Smash(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    attack_name = models.CharField(max_length=50)
    attack_description = models.CharField(max_length=1000)
    image = models.ImageField(default="default.png")

class Up_Smash(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    attack_name = models.CharField(max_length=50)
    attack_description = models.CharField(max_length=1000)
    image = models.ImageField(default="default.png")

class Down_Smash(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    attack_name = models.CharField(max_length=50)
    attack_description = models.CharField(max_length=1000)
    image = models.ImageField(default="default.png")

class Dash_Attack(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    attack_name = models.CharField(max_length=50)
    attack_description = models.CharField(max_length=1000)
    image = models.ImageField(default="default.png")

class Neutral_Arial(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    attack_name = models.CharField(max_length=50)
    attack_description = models.CharField(max_length=1000)
    image = models.ImageField(default="default.png")

class Forward_Arial(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    attack_name = models.CharField(max_length=50)
    attack_description = models.CharField(max_length=1000)
    image = models.ImageField(default="default.png")

class Backward_Arial(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    attack_name = models.CharField(max_length=50)
    attack_description = models.CharField(max_length=1000)
    image = models.ImageField(default="default.png")

class Up_Arial(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    attack_name = models.CharField(max_length=50)
    attack_description = models.CharField(max_length=1000)
    image = models.ImageField(default="default.png")

class Down_Arial(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    attack_name = models.CharField(max_length=50)
    attack_description = models.CharField(max_length=1000)
    image = models.ImageField(default="default.png")

class Forward_Throw(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    attack_name = models.CharField(max_length=50)
    attack_description = models.CharField(max_length=1000)
    image = models.ImageField(default="default.png")

class Backward_Throw(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    attack_name = models.CharField(max_length=50)
    attack_description = models.CharField(max_length=1000)
    image = models.ImageField(default="default.png")

class Up_Throw(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    attack_name = models.CharField(max_length=50)
    attack_description = models.CharField(max_length=1000)
    image = models.ImageField(default="default.png")

class Down_Throw(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    attack_name = models.CharField(max_length=50)
    attack_description = models.CharField(max_length=1000)
    image = models.ImageField(default="default.png")

class Neutral_Special(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    attack_name = models.CharField(max_length=50)
    attack_description = models.CharField(max_length=1000)
    image = models.ImageField(default="default.png")

class Side_Special(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    attack_name = models.CharField(max_length=50)
    attack_description = models.CharField(max_length=1000)
    image = models.ImageField(default="default.png")

class Up_Special(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    attack_name = models.CharField(max_length=50)
    attack_description = models.CharField(max_length=1000)
    image = models.ImageField(default="default.png")

class Down_Special(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    attack_name = models.CharField(max_length=50)
    attack_description = models.CharField(max_length=1000)
    image = models.ImageField(default="default.png")

class Final_Smash(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    attack_name = models.CharField(max_length=50)
    attack_description = models.CharField(max_length=1000)
    image = models.ImageField(default="default.png")

Character.neutral_attack = models.ForeignKey(Neutral_Attack, on_delete=models.CASCADE)
Character.forward_tilt = models.ForeignKey(Forward_Tilt, on_delete=models.CASCADE)
Character.up_tilt = models.ForeignKey(Up_Tilt, on_delete=models.CASCADE)
Character.down_tilt = models.ForeignKey(Down_Tilt, on_delete=models.CASCADE)
Character.forward_smash = models.ForeignKey(Forward_Smash, on_delete=models.CASCADE)
Character.up_smash = models.ForeignKey(Up_Smash, on_delete=models.CASCADE)
Character.down_smash = models.ForeignKey(Down_Smash, on_delete=models.CASCADE)
Character.dash_attack = models.ForeignKey(Dash_Attack, on_delete=models.CASCADE)
Character.neutral_arial = models.ForeignKey(Neutral_Arial, on_delete=models.CASCADE)
Character.forward_arial = models.ForeignKey(Forward_Arial, on_delete=models.CASCADE)
Character.backward_arial = models.ForeignKey(Backward_Arial, on_delete=models.CASCADE)
Character.up_arial = models.ForeignKey(Up_Arial, on_delete=models.CASCADE)
Character.down_arial = models.ForeignKey(Down_Arial, on_delete=models.CASCADE)
Character.forward_throw = models.ForeignKey(Forward_Throw, on_delete=models.CASCADE)
Character.backward_throw = models.ForeignKey(Backward_Throw, on_delete=models.CASCADE)
Character.up_throw = models.ForeignKey(Up_Throw, on_delete=models.CASCADE)
Character.down_throw = models.ForeignKey(Down_Throw, on_delete=models.CASCADE)
Character.neutral_special = models.ForeignKey(Neutral_Special, on_delete=models.CASCADE)
Character.side_special = models.ForeignKey(Side_Special, on_delete=models.CASCADE)
Character.up_special = models.ForeignKey(Up_Special, on_delete=models.CASCADE)
Character.down_special = models.ForeignKey(Down_Special, on_delete=models.CASCADE)
Character.final_smash = models.ForeignKey(Final_Smash, on_delete=models.CASCADE)
