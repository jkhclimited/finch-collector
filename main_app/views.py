from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render(request, 'about.html')

def finch_index(request):
    return render(request, 'finches/index.html', { 'finches': finches })

class Finch:
    def __init__(self, name, breed, scientific_name, color):
        self.name = name
        self.breed = breed
        self.scientific_name = scientific_name
        self.color = color

finches = [
    Finch('Bluey', 'Blue Jay', 'Cyanocitta cristata', 'Blue and White'),
    Finch('Atticus', 'Human', 'Homo Sapien', 'Skin colour?'),
    Finch('Brighty', 'Northern Cardinal', 'Cardinalis cardinalis', 'Bright Red'),
]