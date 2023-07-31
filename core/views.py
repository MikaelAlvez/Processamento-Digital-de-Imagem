from django.shortcuts import render
from .models import Pessoa
# Create your views here.

def home(request):
    Pessoas = Pessoa.objects.all()
    return render(request, "index.html", {"Pessoas:": Pessoas})