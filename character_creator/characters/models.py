# Import modules
import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=50)
    series = models.CharField(max_length=50)
    description = models.CharField(max_length=2000)
    char_image = models.ImageField(default="default.png")
    pub_date = models.DateTimeField(auto_now_add=True)

class Moveset(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    attack_name = models.CharField(max_length=50)
    attack_type = models.CharField(max_length=50)
    attack_description = models.CharField(max_length=1000)
    image = models.ImageField(default="default.png")
