__author__ = "Sebastian Mischke"

import numpy as np
from .game import Game


class Obstacles(Game):
    def __init__(self, grid_size=10):
        self.grid_size = grid_size
        self.won = False
        self.reset()

    def reset(self):
        self.board = np.zeros((self.grid_size, self.grid_size))
        self.player = (int(self.grid_size / 2), self.grid_size - 1)

    @property
    def name(self):
        return "Obstacles"

    @property
    def nb_actions(self):
        return 5

    def play(self, action):
        state = self.state
        if action == 0:
            action = -1
        elif action == 1:
            action = 0
        else:
            action = 1
        f0, f1, basket = state[0]
        new_basket = min(max(1, basket + action), self.grid_size - 1)
        f0 += 1
        out = np.asarray([f0, f1, new_basket])
        out = out[np.newaxis]
        assert len(out.shape) == 2
        self.state = out

    def get_state(self):
        canvas = copy.deepcopy(self.board)
        canvas[self.player] = 2
        return np.asarray(canvas)

    def get_score(self):
        if self.board[self.player] is 1:
            return -1
        else:
            return 0

    def is_over(self):
        return self.board[self.player] is 1

    def is_won(self):
        fruit_row, fruit_col, basket = self.state[0]
        return fruit_row == self.grid_size - 1 and abs(fruit_col - basket) <= 1
