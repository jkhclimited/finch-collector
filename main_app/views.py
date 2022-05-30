from ast import Del, Delete
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Card, EffectType
from .forms import OwnedForm

class CardCreate(LoginRequiredMixin, CreateView):
    model = Card
    fields = ['name', 'card_type', 'attribute', 'type', 'level', 'atk', 'defense', 'property', 'description']
    success_url = '/cards/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class CardUpdate(LoginRequiredMixin, UpdateView):
    model = Card
    fields = '__all__'

class CardDelete(LoginRequiredMixin, DeleteView):
    model = Card
    success_url = '/cards/'

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def cards_index(request):
    cards = Card.objects.filter(user=request.user)
    return render(request, 'cards/index.html', {'cards': cards})

@login_required
def card_details(request, card_id):
    card = Card.objects.get(id=card_id)
    effect_types_not_on_card = EffectType.objects.exclude(id__in = card.effect_type.all().values_list('id'))
    owned_form = OwnedForm()
    return render(request, 'cards/detail.html', { 
        'card': card, 
        'owned': owned_form,
        'effects': effect_types_not_on_card,
    })

@login_required
def add_copies(request, card_id):
    form = OwnedForm(request.POST)
    if form.is_valid():
        new_copies = form.save(commit=False)
        new_copies.card_id = card_id
        new_copies.save()
    return redirect('detail', card_id=card_id)

@login_required
def assoc_effect(request, card_id, effect_id):
    Card.objects.get(id=card_id).effect_type.add(effect_id)
    return redirect('detail', card_id=card_id)

@login_required
def disassoc_effect(request, card_id, effect_id):
    Card.objects.get(id=card_id).effect_type.remove(effect_id)
    return redirect('detail', card_id=card_id)

class EffectList(LoginRequiredMixin, ListView):
    model = EffectType

class EffectDetail(LoginRequiredMixin, DetailView):
    model = EffectType

class EffectCreate(LoginRequiredMixin, CreateView):
    model = EffectType
    fields = '__all__'

class EffectUpdate(LoginRequiredMixin, UpdateView):
    model = EffectType 
    fields = '__all__'

class EffectDelete(LoginRequiredMixin, DeleteView):
    model = EffectType
    success_url = '/effects/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)