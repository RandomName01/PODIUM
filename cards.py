from collections import namedtuple

Card = namedtuple('Card', 'color number')
deck = [Card(color=col, number=num) for col in ["hearts", "diamonds", "spades", "clubs"]
        for num in range(1, 14)]

jokers = [Card(color="joker", number=14) for _ in range(2)]

FULL_DECK = deck + jokers
