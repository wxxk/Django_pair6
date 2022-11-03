from django.shortcuts import render, redirect
from .models import CustomCard

# Create your views here.
def index(request):
    cards = CustomCard.objects.all()[:10]
    card_list = []
    for card in cards:

        if "mcd" not in card.image:
            card_list.append(card)

    context = {
        "cards": card_list,
    }

    return render(request, "community/index.html", context)


def rule(request):
    return render(request, "community/rule.html")
