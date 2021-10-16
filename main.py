from cards import FULL_DECK
from copy import deepcopy
import random
from collections import deque

c = deque(deepcopy(FULL_DECK))
random.shuffle(c)
playing_board = []

for a in range(7):
    playing_board.append([c.pop() for _ in range(a+1)])

print(playing_board)
