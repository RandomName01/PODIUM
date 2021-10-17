from collections import namedtuple

# HACK: turned sera modifiable en utilisant la fonction flip_card
Card = namedtuple('Card', 'color number flipped')

DECK = [Card(color=col, number=num, flipped=False)
        for col in ["hearts", "diamonds", "spades", "clubs"]
        for num in range(1, 14)]

JOKERS = [Card(color="joker", number=14, flipped=False) for _ in range(2)]

# TADA! Le jeu de cartes complet est déjà créé en à peine quelques lignes. et oui!
FULL_DECK = DECK + JOKERS


def flip_card(card: Card) -> Card:
    return card._replace(flipped=not card.flipped)
