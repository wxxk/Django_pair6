from pokemontcgsdk import Card
from pokemontcgsdk import Set
from pokemontcgsdk import Type
from pokemontcgsdk import Supertype
from pokemontcgsdk import Subtype
from pokemontcgsdk import Rarity
from pokemontcgsdk import RestClient

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pjt.settings")
import django

django.setup()
from community.models import CustomCard

RestClient.configure("f6f78c7a-0355-450e-9178-813d22bb50c0")


def test_card():
    cards = Card.where(q="supertype:Pokémon")

    data = {}

    for card in cards:
        data[card.name] = {
            "types": card.types[0],
            "supertype": card.supertype,
            "image": card.images.small,
        }

    return data


if __name__ == "__main__":
    card_dict = test_card()
    for t, l in card_dict.items():
        CustomCard(
            name=t, types=l["types"], supertype=l["supertype"], image=l["image"]
        ).save()
