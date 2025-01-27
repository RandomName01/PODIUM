from cards import FULL_DECK, Card, flip_card
from copy import deepcopy
import random
from collections import deque
from typing import List


c = deque(deepcopy(FULL_DECK))
random.shuffle(c)


playing_board: List[List[Card]] = []

for a in range(7):
    stack = [c.pop() for _ in range(a+1)]
    playing_board.append([flip_card(stack[0])] + stack[1:])

    # print(playing_board)
