from django.shortcuts import render, redirect
from .models import CustomCard

# Create your views here.
def index(request):
    cards = CustomCard.objects.all()
    context = {
        "cards": cards,
    }
    return render(request, "community/index.html", context)


def rule(request):
    return render(request, "community/rule.html")
