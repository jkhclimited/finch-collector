from django.contrib import admin
from .models import Card, EffectType, Owned

admin.site.register(Card)
admin.site.register(Owned)
admin.site.register(EffectType)