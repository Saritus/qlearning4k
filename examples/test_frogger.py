from keras.models import Sequential
from keras.layers import *
from qlearning4k.games import Frogger
from keras.optimizers import *
from qlearning4k import Agent

rows = 10
cols = 10
hidden_size = 100
nb_frames = 1

model = Sequential()
model.add(Flatten(input_shape=(nb_frames, rows, cols)))
model.add(Dense(hidden_size, activation='relu'))
model.add(Dense(hidden_size, activation='relu'))
model.add(Dense(5, activation='softmax'))
model.compile(sgd(lr=.2), "mse")

game = Frogger(rows, cols)
agent = Agent(model=model)
agent.train(game, batch_size=50, nb_epoch=10000, epsilon_rate=0.2)
agent.play(game, nb_epoch=10)
