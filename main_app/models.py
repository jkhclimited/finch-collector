from django.db import models
from django.urls import reverse
from django.forms import IntegerField
from django.contrib.auth.models import User

COPIES = (
    ('1', 'Single (1)'),
    ('2', 'Pair (2)'),
    ('3', 'Playset (3)')
)

class EffectType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('effect_detail', kwargs={'pk': self.id})


class Card(models.Model):
    name = models.CharField(max_length=100)
    card_type = models.CharField(max_length=20)
    attribute = models.CharField(max_length=20, default='N/A')
    type = models.CharField(max_length=100, default='N/A')
    level = models.IntegerField(default=0)
    atk = models.IntegerField(default=0)
    defense = models.IntegerField(default=0)
    property = models.CharField(max_length=20, default='N/A')
    description = models.TextField(max_length=1000)
    effect_type = models.ManyToManyField(EffectType)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'card_id': self.id})
    
    def got_playset(self):
        return self.owned_set.filter(copies = 3)

class Owned(models.Model):
    set = models.CharField(max_length=40)
    copies = models.CharField(
        max_length=1,
        choices=COPIES,
        default=COPIES[0][0]
    )

    card = models.ForeignKey(Card, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_copies_display()} from {self.set}"
    
    class Meta:
        ordering = ['set']