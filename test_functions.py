from cards import Card
from main import playing_board


def pretty_cards(card: Card) -> str:
    """
    Function that prettifies cards.
    If the card is flipped, its contents will be surrounded by parenthses,
    otherwise, they will be surrounded by square brackets.
    """
    card_symbol = {"spades":  '♤',
                   "clubs": '♧',
                   "hearts": '♡',
                   "diamonds": '◇',
                   "joker": '笑'}

    if card.flipped:
        return f"({card.number}{card_symbol[card.color]})"
    return f"[{card.number}{card_symbol[card.color]}]"


if __name__ == '__main__':
    for stack in playing_board:
        print([pretty_cards(cards) for cards in stack])

