from collections import namedtuple

# HACK: turned sera modifiable en utilisant la méthode ._replace()
Card = namedtuple('Card', 'color number flipped')

deck = [Card(color=col, number=num, flipped=False)
        for col in ["hearts", "diamonds", "spades", "clubs"]
        for num in range(1, 14)]

jokers = [Card(color="joker", number=14, flipped=False) for _ in range(2)]

# TADA! Le jeu de cartes complet est déjà créé en à peine quelques lignes. et oui!
FULL_DECK = deck + jokers
