from keras.models import Sequential
from keras.layers import Flatten, Dense
from qlearning4k.games import Obstacles
from keras.optimizers import *
from qlearning4k import Agent

grid_size = 10
hidden_size = 100
nb_frames = 1

model = Sequential()
model.add(Flatten(input_shape=(nb_frames, grid_size, grid_size)))
model.add(Dense(hidden_size, activation='relu'))
model.add(Dense(hidden_size, activation='relu'))
model.add(Dense(5))
model.compile(sgd(lr=.2), "mse")

game = Obstacles(grid_size)
agent = Agent(model=model)
agent.train(game, batch_size=10, nb_epoch=1000, epsilon=.1)
agent.play(game)
