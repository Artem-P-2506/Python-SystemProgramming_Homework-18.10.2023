import threading
from Snake import *
from Field import *
import random

directionsOfMovement = ["NONE", "UP", "DOWN", "LEFT", "RIGHT"]

class Game:
    def __init__(self):
        self._field = Field()
        self._snake = Snake()

    def startGame(self):
        field = self._field.getField()
        self._snake.addNewHead(random.randint(0, len(field) - 1), random.randint(0, len(field[0]) - 1), self._field)
        self._snake.setDirectionOfMovement(directionsOfMovement[random.randint(1, 4)])
        self._snake.setSnakeOnField(self._field)

        showingThread = threading.Thread(target=self._field._showField, args=())
        showingThread.start()

        inputThread = threading.Thread(target=self._snake.changeDirection(), args=())
        inputThread.start()

        while(self._snake.getIsAlive()):
            self._snake.move(self._field)