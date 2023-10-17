import threading
import time
from Snake import *
from Field import *
import random

dirictionsOfMovement = ["NONE", "UP", "DOWN", "LEFT", "RIGHT"]

class Game:
    def __init__(self):
        self._field = Field()
        self._snake = Snake()

    def startGame(self):
        field = self._field.getField()
        self._snake.setCoordinateX(random.randint(0, len(field) - 1))
        self._snake.setCoordinateY(random.randint(0, len(field[0]) - 1))
        self._field.setSnakeOnField(self._snake)

        isSnakeAlive = True
        while(isSnakeAlive):
            self._snake.setDirectionOfMovement(dirictionsOfMovement[1])
            self._snake.move(self._field)
            showingThread = threading.Thread(target=self._field._showField, args=())
            showingThread.start()
            time.sleep(0.5)