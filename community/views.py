from django.shortcuts import render, redirect
from .models import CustomCard
import random

# Create your views here.
def index(request):
    cards = CustomCard.objects.all()
    card_list = []

    dec1_cards = [
        "https://cards.image.pokemonkorea.co.kr/data/wmimages/S/S11/S11_056.png?w=512",
        "https://cards.image.pokemonkorea.co.kr/data/wmimages/S/S9a/S9a_058.png?w=512",
        "https://cards.image.pokemonkorea.co.kr/data/wmimages/S/S8a/S8a_013.png?w=512",
        "https://cards.image.pokemonkorea.co.kr/data/wmimages/S/S10b/S10b_060.png?w=512",
        "https://cards.image.pokemonkorea.co.kr/data/wmimages/S/S8b/S8b_099.png?w=512",
        "https://cards.image.pokemonkorea.co.kr/data/wmimages/S/S9/S9_082.png?w=512",
        "https://cards.image.pokemonkorea.co.kr/data/wmimages/S/S11/S11_057.png?w=512",
        "https://cards.image.pokemonkorea.co.kr/data/wmimages/S/S9a/S9a_043.png?w=512",
    ]

    for card in cards:
        if "mcd" not in card.image:
            card_list.append(card)

    # print(dec1_cards)

    card_list = random.sample(card_list, 6)
    context = {
        "cards": card_list,
        "dec1": dec1_cards,
    }

    return render(request, "community/index.html", context)


def rule(request):
    return render(request, "community/rule.html")
