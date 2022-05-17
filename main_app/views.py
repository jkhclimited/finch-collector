from django.shortcuts import render
from django.http import HttpResponse
from .models import Card

def home(request):
    return HttpResponse('<h1>This is a test</h1>')

def about(request):
    return render(request, 'about.html')

def cards_index(request):
    cards = Card.objects.all()
    return render(request, 'cards/index.html', {'cards': cards})

def card_details(request, card_id):
    card = Card.objects.get(id=card_id)
    return render(request, 'cards/detail.html', { 'card': card})