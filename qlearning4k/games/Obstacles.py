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
        # Left
        if (action is 0
            and self.player[0] > 0
            and self.board[self.player[0] - 1, self.player[1]] is 0):
            self.player[0] -= 1
        # Right
        elif (action is 1
              and self.player[0] < self.grid_size - 1
              and self.board[self.player[0] + 1, self.player[1]] is 0):
            self.player[0] += 1
        # Up
        elif (action is 2
              and self.player[1] > 0
              and self.board[self.player[0], self.player[1] - 1] is 0):
            self.player[1] -= 1
        # Down
        elif (action is 3
              and self.player[1] > self.grid_size - 1
              and self.board[self.player[0], self.player[1] + 1] is 0):
            self.player[1] += 1

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
