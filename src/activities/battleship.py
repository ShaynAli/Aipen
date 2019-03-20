from activities.activities import Activity
from enum import Enum
from itertools import cycle, chain
from collections import Counter
from random import shuffle
from typing import List


class Location(Enum):
    UNKNOWN = -1
    HIT = 5
    MISS = 0


class Battleship(Activity):
    n_players = 2
    n_rows = n_cols = 10
    n_turns = 0
    n_ships = 10
    ship_length = 3
    placement = True

    @staticmethod
    def new_grid():
        return [[Location.UNKNOWN for _ in range(Battleship.n_rows)] for _ in range(Battleship.n_rows)]

    def __init__(self, players: List[Activity.Agent]):
        super().__init__()
        self.players = cycle(players)
        shuffle(self.players)
        self.current_player = next(self.players)
        self.boards = {p: Battleship.new_grid() for p in self.players}

    def state(self, agent):
        return self.boards[agent]

    def score(self, agent):
        board_entries = chain(*self.boards[agent])
        counter = Counter(board_entries)
        total = 0
        for k, v in counter:
            total += k * v
        return total

    class Action:
        place_ship = 'place'
        launch_missile = 'missile'

        def __init__(self, action_type, *locations):
            self.action_type = action_type
            self.locations = locations

    def actions(self, agent):
        board = self.boards[agent]
        # TODO: Encapsulate state about ship placement and turns for placing ships
        if self.placement:
            # self.act(self, self.current_player, self.Action.place_ship)
            # FROM own.board, return (row i, col j) for i e 0..9, j e 1..8
            # EXCEPT where SHIP exists, defined by center point
            # DEF 1) Ships are defined by a central point, have length 3, and can only be placed horizontally
                # initially, all points except for the far columns are valid
                # once a ship has been placed, mark off the spaces taken up by it
            pass
        else:
            # self.act(self, self.current_player, self.Action.launch_missile)
            return [(row, col) for row, col in zip(enumerate(board), enumerate(board))
                    if board[row][col] == Location.UNKNOWN]

    def act(self, agent, *actions):
        if agent != self.current_player:
            return

        if not actions:
            self.current_player = next(self.players)
            return

        super().act(agent, actions)

        action = actions[0]
        if action.action_type == 'place':
            # from list of actions, choose a valid move, selecting a point X
            # once X is selected, mark off (1) the left and right spaces
            # mark X as Location.HIT or Location.MISS if it collides with a ship
            self.n_turns += 1
            self.n_ships -= 1
            if self.n_ships <= 0:
                self.placement = False

        if action.action_type == 'missile':
            # guess a new target and fire
            pass
