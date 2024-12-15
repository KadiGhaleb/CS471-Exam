from django.shortcuts import render
from .models import Game, Developer
# Create your views here.


def home(request):
    return render(request, 'app1/home.html')


def list(request):
    games = Game.objects.all()
    return render(request, 'app1/list.html', {'games':games})
