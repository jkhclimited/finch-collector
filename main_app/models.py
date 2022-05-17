from django.db import models
from django.forms import IntegerField

# Create your models here.
class Card(models.Model):
    card_type = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    attribute = models.CharField(max_length=20)
    type = models.CharField(max_length=100)
    level = models.IntegerField()
    atk = models.IntegerField()
    defense = models.IntegerField()
    property = models.CharField(max_length=20)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.name