__author__ = "Sebastian Mischke"

import numpy as np
from .game import Game
import copy


class Obstacles(Game):
    def __init__(self, grid_size=10):
        self.grid_size = grid_size
        self.won = False
        self.reset()

    def reset(self):
        self.board = np.zeros((self.grid_size, self.grid_size))
        self.player = [self.grid_size - 1, int(self.grid_size / 2)]

    @property
    def name(self):
        return "Obstacles"

    @property
    def nb_actions(self):
        return 5

    def play(self, action):
        # Up
        if (action == 0
            and self.player[0] > 0
            and self.board[self.player[0] - 1, self.player[1]] == 0):
            self.player[0] -= 1
        # Down
        elif (action == 1
              and self.player[0] < self.grid_size - 1
              and self.board[self.player[0] + 1, self.player[1]] == 0):
            self.player[0] += 1
        # Left
        elif (action == 2
              and self.player[1] > 0
              and self.board[self.player[0], self.player[1] - 1] == 0):
            self.player[1] -= 1
        # Right
        elif (action == 3
              and self.player[1] < self.grid_size - 1
              and self.board[self.player[0], self.player[1] + 1] == 0):
            self.player[1] += 1

        self.board = np.roll(self.board, 1, axis=0)
        self.board[0] = np.zeros(self.grid_size)
        self.board[0][np.random.randint(0, self.grid_size)] = 1

    def get_state(self):
        canvas = copy.deepcopy(self.board)
        canvas[self.player[0], self.player[1]] = 2
        return np.asarray(canvas)

    def get_score(self):
        if self.board[self.player[0], self.player[1]] == 1:
            return -1
        else:
            return 0

    def is_over(self):
        return self.board[self.player[0], self.player[1]] == 1

    def is_won(self):
        return False
