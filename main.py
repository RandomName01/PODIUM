from cards import FULL_DECK, Cards
from copy import deepcopy
import random
from collections import deque
from typing import List


c = deque(deepcopy(FULL_DECK))
random.shuffle(c)


playing_board: List[List[Cards]] = []

for a in range(7):
    playing_board.append([c.pop() for _ in range(a+1)])

    # print(playing_board)
