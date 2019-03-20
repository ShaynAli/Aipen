from activities.activities import Activity
from enum import Enum
from itertools import cycle, chain
from collections import Counter
from random import shuffle
from typing import List

class Carve(Enum):
    UNKNOWN = -1
    NOISE = 0
    DECODED = 1

class Fingerprint(Activity):
    n_bytes = 8
    
    @staticmethod
    def new_grid():
        return [[CARVE.UNKNOWN for _ in range(Fingerprint.n_bytes)] for _ in range(Fingerprint.n_bytes)]
