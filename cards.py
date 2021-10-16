from collections import namedtuple

# HACK: turned sera modifiable en utilisant la méthode ._replace()
Card = namedtuple('Card', 'color number turned')

deck = [Card(color=col, number=num, turned=False) for col in ["hearts", "diamonds", "spades", "clubs"]
        for num in range(1, 14)]

jokers = [Card(color="joker", number=14, turned=False) for _ in range(2)]

# TADA! Le jeu de cartes complet est déjà créé en à peine quelques lignes.
FULL_DECK = deck + jokers
