from ast import Del, Delete
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Card, EffectType
from .forms import OwnedForm

class CardCreate(CreateView):
    model = Card
    fields = '__all__'
    success_url = '/cards/'

class CardUpdate(UpdateView):
    model = Card
    fields = '__all__'

class CardDelete(DeleteView):
    model = Card
    success_url = '/cards/'

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cards_index(request):
    cards = Card.objects.all()
    return render(request, 'cards/index.html', {'cards': cards})

def card_details(request, card_id):
    card = Card.objects.get(id=card_id)
    effect_types_not_on_card = EffectType.objects.exclude(id__in = card.effect_type.all().values_list('id'))
    owned_form = OwnedForm()
    return render(request, 'cards/detail.html', { 
        'card': card, 
        'owned': owned_form,
        'effects': effect_types_not_on_card,
    })

def add_copies(request, card_id):
    form = OwnedForm(request.POST)
    if form.is_valid():
        new_copies = form.save(commit=False)
        new_copies.card_id = card_id
        new_copies.save()
    return redirect('detail', card_id=card_id)

def assoc_effect(request, card_id, effect_id):
    Card.objects.get(id=card_id).effect_type.add(effect_id)
    return redirect('detail', card_id=card_id)

class EffectList(ListView):
    model = EffectType

class EffectDetail(DetailView):
    model = EffectType

class EffectCreate(CreateView):
    model = EffectType
    fields = ['name']

class EffectUpdate(UpdateView):
    model = EffectType 
    fields = ['name']

class EffectDelete(DeleteView):
    model = EffectType
    success_url = '/cards/'