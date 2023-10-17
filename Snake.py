dirictions = ["NONE", "UP", "DOWN", "LEFT", "RIGHT"]

class Snake:
    def __init__(self):
        self._CoordinateX = -1
        self._CoordinateY = -1
        self._headSimbol = "$"
        self._simbol = "+"
        self._size = 1
        self._directionOfMovement = dirictions[0]

    def getCoordinateX(self):
        return self._CoordinateX

    def getCoordinateY(self):
        return self._CoordinateY

    def getHeadSimbol(self):
        return self._headSimbol

    def getBodySimbol(self):
        return self._simbol

    def getSize(self):
        return self._size

    def getDirectionOfMovement(self):
        return self._directionOfMovement

    def setCoordinateX(self, newCoordinateX):
        self._CoordinateX = newCoordinateX

    def setCoordinateY(self, newCoordinateY):
        self._CoordinateY = newCoordinateY

    def setDirectionOfMovement(self, newDirection):
        self._directionOfMovement = newDirection

    # def setSnakeOnField(self, fieldOBJ):
    #     fieldOBJ[self._CoordinateX][self._CoordinateY] = self._headSimbol

    def move(self, fieldOBJ):
        if self._directionOfMovement == dirictions[1]: # UP
            if 0 <= self._CoordinateY - 1:
                self._CoordinateY -= 1
            else:
                self._CoordinateY = fieldOBJ.getFieldSize() - 1
        elif self._directionOfMovement == dirictions[2]: # DOWN
            if self._CoordinateY + 1 < fieldOBJ.getFieldSize():
                self._CoordinateY += 1
            else:
                self._CoordinateY = 0
        elif self._directionOfMovement == dirictions[3]: # LEFT
            if 0 <= self._CoordinateX - 1:
                self._CoordinateX -= 1
            else:
                self._CoordinateX = fieldOBJ.getFieldSize() - 1
        elif self._directionOfMovement == dirictions[4]: # RIGHT
            if self._CoordinateX + 1 < fieldOBJ.getFieldSize():
                self._CoordinateX += 1
            else:
                self._CoordinateX = 0
        else:
            print("Invalid direction given!")