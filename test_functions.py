from cards import Card
from main import playing_board

def pretty_cards(card: Card) -> str:
    """
    Prettify cards.
    If the card is flipped, then, its contents will be surroundedby parenthses,
    otherwise, they wille be surrounded by square brackets.
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

