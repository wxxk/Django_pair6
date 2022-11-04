from django.shortcuts import render, redirect
from .models import CustomCard
import random

# Create your views here.
def index(request):
    cards = CustomCard.objects.all()
    card_list = []

    dec1_cards = [
        "https://cards.image.pokemonkorea.co.kr/data/wmimages/S/S11/S11_056.png",
        "https://cards.image.pokemonkorea.co.kr/data/wmimages/S/S9a/S9a_058.png",
        "https://cards.image.pokemonkorea.co.kr/data/wmimages/S/S8a/S8a_013.png",
        "https://cards.image.pokemonkorea.co.kr/data/wmimages/S/S10b/S10b_060.png",
        "https://cards.image.pokemonkorea.co.kr/data/wmimages/S/S8b/S8b_099.png",
        "https://cards.image.pokemonkorea.co.kr/data/wmimages/S/S9/S9_082.png",
        "https://cards.image.pokemonkorea.co.kr/data/wmimages/S/S11/S11_057.png",
        "https://cards.image.pokemonkorea.co.kr/data/wmimages/S/S9a/S9a_043.png",
        "https://cards.image.pokemonkorea.co.kr/data/wmimages/S/SJ/SJ_021.png",
        "https://cards.image.pokemonkorea.co.kr/data/wmimages/S/SL/SLD_015.png",
        "https://cards.image.pokemonkorea.co.kr/data/wmimages/S/S7/S7D_059.png",
        "https://cards.image.pokemonkorea.co.kr/data/wmimages/S/SI/SI_377.png",
        "https://cards.image.pokemonkorea.co.kr/data/wmimages/S/S8b/S8b_132.png",
        "https://cards.image.pokemonkorea.co.kr/data/wmimages/S/SL/SLL_015.png",
        "https://cards.image.pokemonkorea.co.kr/data/wmimages/S/S8b/S8b_146.png",
        "https://cards.image.pokemonkorea.co.kr/data/wmimages/S/SL/SLD_017.png",
        "https://cards.image.pokemonkorea.co.kr/data/wmimages/S/S8b/S8b_153.png",
        "https://cards.image.pokemonkorea.co.kr/data/wmimages/S/SI/SI_396.png",
        "https://cards.image.pokemonkorea.co.kr/data/wmimages/S/S10/S10P_065.png",
        "https://cards.image.pokemonkorea.co.kr/data/wmimages/S/S10a/S10a_071.png",
        "https://cards.image.pokemonkorea.co.kr/data/wmimages/S/S10b/S10b_099.png",
        "https://cards.image.pokemonkorea.co.kr/data/wmimages/S/SL/SLL_021.png",
        "https://cards.image.pokemonkorea.co.kr/data/wmimages/S/S8b/S8b_176.png",
    ]

    dec2_cards = [
        "https://cards.image.pokemonkorea.co.kr/data/wmimages/S/SL/SLD_001.png",
        "https://cards.image.pokemonkorea.co.kr/data/wmimages/S/SI/SI_171.png",
        "https://cards.image.pokemonkorea.co.kr/data/wmimages/S/S10/S10D_048.png",
        "https://cards.image.pokemonkorea.co.kr/data/wmimages/S/S8b/S8b_117.png",
        "https://cards.image.pokemonkorea.co.kr/data/wmimages/S/S10/S10D_049.png",
        "https://cards.image.pokemonkorea.co.kr/data/wmimages/S/SP6/SP6_004.png",
        "https://cards.image.pokemonkorea.co.kr/data/wmimages/S/S9a/S9a_026.png",
        "https://cards.image.pokemonkorea.co.kr/data/wmimages/S/SJ/SJ_018.png",
        "https://cards.image.pokemonkorea.co.kr/data/wmimages/S/SL/SLD_012.png",
        "https://cards.image.pokemonkorea.co.kr/data/wmimages/S/S8b/S8b_141.png",
        "https://cards.image.pokemonkorea.co.kr/data/wmimages/S/S10/S10D_062.png",
        "https://cards.image.pokemonkorea.co.kr/data/wmimages/S/SL/SLD_015.png",
        "https://cards.image.pokemonkorea.co.kr/data/wmimages/S/SA/SA_W_013.png",
        "https://cards.image.pokemonkorea.co.kr/data/wmimages/S/S10/S10P_062.png",
        "https://cards.image.pokemonkorea.co.kr/data/wmimages/S/S8b/S8b_146.png",
        "https://cards.image.pokemonkorea.co.kr/data/wmimages/SM/SM11a/SM11a_051.png",
        "https://cards.image.pokemonkorea.co.kr/data/wmimages/S/SL/SLD_018.png",
        "https://cards.image.pokemonkorea.co.kr/data/wmimages/S/S5a/S5a_067.png",
        "https://cards.image.pokemonkorea.co.kr/data/wmimages/S/S9a/S9a_065.png",
        "https://cards.image.pokemonkorea.co.kr/data/wmimages/S/S11/S11_096.png",
        "https://cards.image.pokemonkorea.co.kr/data/wmimages/S/S4a/S4a_178.png",
        "https://cards.image.pokemonkorea.co.kr/data/wmimages/S/S4a/S4a_182.png",
        "https://cards.image.pokemonkorea.co.kr/data/wmimages/S/S8b/S8b_169.png",
        "https://cards.image.pokemonkorea.co.kr/data/wmimages/S/S10b/S10b_101.png",
    ]

    for card in cards:
        if "mcd" not in card.image:
            card_list.append(card)

    card_list = random.sample(card_list, 6)
    context = {
        "cards": card_list,
        "dec1": dec1_cards,
        "dec2": dec2_cards,
    }

    return render(request, "community/index.html", context)


def rule(request):
    return render(request, "community/rule.html")
