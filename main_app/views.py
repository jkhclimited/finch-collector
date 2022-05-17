from ast import Del, Delete
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Card
from .forms import OwnedForm


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cards_index(request):
    cards = Card.objects.all()
    return render(request, 'cards/index.html', {'cards': cards})

def card_details(request, card_id):
    card = Card.objects.get(id=card_id)
    owned_form = OwnedForm()
    return render(request, 'cards/detail.html', { 
        'card': card, 'owned': owned_form    
    })

def add_copies(request, card_id):
    form = OwnedForm(request.POST)
    if form.is_valid():
        new_copies = form.save(commit=False)
        new_copies.card_id = card_id
        new_copies.save()
    return redirect('detail', card_id=card_id)

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

