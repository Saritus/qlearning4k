__author__ = "Sebastian Mischke"

import numpy as np
from .game import Game
import copy


class Frogger(Game):
    def __init__(self, rows=10, cols=10):
        self.rows = rows
        self.cols = cols
        self.won = False
        self.reset()

    def reset(self):
        self.board = self.create_board()
        self.player = [self.rows - 1, int(self.cols / 2)]

    def create_board(self):
        board = np.zeros((self.rows, self.cols))
        return board

    @property
    def name(self):
        return "Frogger"

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
              and self.player[0] < self.rows - 1
              and self.board[self.player[0] + 1, self.player[1]] == 0):
            self.player[0] += 1
        # Left
        elif (action == 2
              and self.player[1] > 0
              and self.board[self.player[0], self.player[1] - 1] == 0):
            self.player[1] -= 1
        # Right
        elif (action == 3
              and self.player[1] < self.cols - 1
              and self.board[self.player[0], self.player[1] + 1] == 0):
            self.player[1] += 1

        self.board = np.roll(self.board, 1, axis=0)
        self.board[0] = np.zeros(self.cols)
        self.board[0][np.random.randint(0, self.cols)] = 1

    def get_state(self):
        canvas = copy.deepcopy(self.board)
        canvas[self.player[0], self.player[1]] = 2
        return np.asarray(canvas)

    def get_score(self):
        if self.board[self.player[0], self.player[1]] == 1:
            return -1
        else:
            return self.rows - self.player[0] - 1

    def is_over(self):
        return self.board[self.player[0], self.player[1]] == 1 or self.player[0] == 0

    def is_won(self):
        return self.player[0] == 0
