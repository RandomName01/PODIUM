from cards import Cards

def black_or_red(card: Cards) -> str:
    return "black" if card.color in ("clubs", "spades") else "red"



def can_follow(card_1: Cards, card_2: Cards) -> bool:
    """
    Checks if a card can follow another.
    """
    return black_or_red(card_1) != black_or_red(card_2) & \
        card_1.number - 1 == card_2.number | \
        card_1.color == 'joker'

