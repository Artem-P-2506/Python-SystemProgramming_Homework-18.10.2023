from Point2D import *

directions = ["NONE", "UP", "DOWN", "LEFT", "RIGHT"]

class Snake:
    def __init__(self):
        self._snakeArray = []
        self._headSymbol = "@"
        self._bodySymbol = "*"
        self._size = 1
        self._directionOfMovement = directions[0]
        self._isAlive = True

    def getSnakeArray(self):
        return self._snakeArray

    def getHeadSymbol(self):
        return self._headSymbol

    def getBodySymbol(self):
        return self._bodySymbol

    def getSize(self):
        return self._size

    def getDirectionOfMovement(self):
        return self._directionOfMovement

    def getIsAlive(self):
        return self._isAlive

    # def addNewHead(self, coordinateX, coordinateY):
    #     self._snakeArray.insert(0, Point2D(coordinateX, coordinateY).setSymbol(self._headSymbol))

    def setDirectionOfMovement(self, newDirection):
        self._directionOfMovement = newDirection

    def setSize(self, newSize):
        if 0 <= newSize:
            self._size = newSize

    def snakeIsDead(self):
        self._isAlive = False
        print("Snake is dead!")

    def changeDirection(self):
        while(True):
            choiseDirection = str(input())
            if choiseDirection == "w" or "W" or "ц" or "Ц":
                self.setDirectionOfMovement(directions[1])
            elif choiseDirection == "s" or "S" or "ы" or "Ы":
                self.setDirectionOfMovement(directions[2])
            elif choiseDirection == "a" or "A" or "ф" or "Ф":
                self.setDirectionOfMovement(directions[3])
            elif choiseDirection == "d" or "D" or "в" or "В":
                self.setDirectionOfMovement(directions[4])
            else:
                print("Invalid direction entered!")


    # def addNewHead(self, coordinateX, coordinateY, fieldOBJ):
    #     field = fieldOBJ.getField()
    #     if field[coordinateX][coordinateX] == ".":
    #         if self._size == 1:
    #             if self._snakeArray:
    #                 fieldOBJ.deleteFromField(self._snakeArray[0].getCoordinateX(), self._snakeArray[0].getCoordinateY())
    #                 self._snakeArray.pop()
    #         newHead = Point2D(coordinateX, coordinateY)
    #         newHead.setSymbol(self._headSymbol)
    #         self._snakeArray.insert(0, newHead)
    #         if 1 < self._size:
    #             self._snakeArray[1].setSymbol(self._bodySymbol)
    #     else:
    #         self.snakeIsDead()

    def addNewHead(self, coordinateX, coordinateY, fieldOBJ):
        field = fieldOBJ.getField()
        if field[coordinateX][coordinateY] == ".":
            newHead = Point2D(coordinateX, coordinateY)
            newHead.setSymbol(self._headSymbol)
            self._snakeArray.insert(0, newHead)

            if 1 < self._size:
                self._snakeArray[1].setSymbol(self._bodySymbol)
            if len(self._snakeArray) > self._size:
                fieldOBJ.deleteFromField(self._snakeArray[self._size].getCoordinateX(), self._snakeArray[self._size].getCoordinateY())
                self._snakeArray.pop()
        else:
            self.snakeIsDead()

    def setSnakeOnField(self, fieldOBJ):
        field = fieldOBJ.getField()
        if self._snakeArray:
            for item in self._snakeArray:
                field[item.getCoordinateX()][item.getCoordinateY()] = item.getSymbol()
            fieldOBJ.setField(field)
        else:
            print("Error!")

    def move(self, fieldOBJ):
        # if self._directionOfMovement == dirictions[1]: # UP
        #     if 0 <= self._CoordinateY - 1:
        #         self._CoordinateY -= 1
        #     else:
        #         self._CoordinateY = fieldOBJ.getFieldSize() - 1
        # elif self._directionOfMovement == dirictions[2]: # DOWN
        #     if self._CoordinateY + 1 < fieldOBJ.getFieldSize():
        #         self._CoordinateY += 1
        #     else:
        #         self._CoordinateY = 0
        # elif self._directionOfMovement == dirictions[3]: # LEFT
        #     if 0 <= self._CoordinateX - 1:
        #         self._CoordinateX -= 1
        #     else:
        #         self._CoordinateX = fieldOBJ.getFieldSize() - 1
        # elif self._directionOfMovement == dirictions[4]: # RIGHT
        #     if self._CoordinateX + 1 < fieldOBJ.getFieldSize():
        #         self._CoordinateX += 1
        #     else:
        #         self._CoordinateX = 0

        # UP
        if self._directionOfMovement == directions[1]:
            if 0 <= self._snakeArray[0].getCoordinateX() - 1:
                self.addNewHead(self._snakeArray[0].getCoordinateX() - 1, self._snakeArray[0].getCoordinateY(), fieldOBJ)
                # self._snakeArray[0].setCoordinateX(self._snakeArray[0].getCoordinateX() - 1)
            else:
                self.addNewHead(fieldOBJ.getFieldSize() - 1, self._snakeArray[0].getCoordinateY(), fieldOBJ)
                # self._snakeArray[0].setCoordinateX(fieldOBJ.getFieldSize() - 1)
        # DOWN
        elif self._directionOfMovement == directions[2]:
            if self._snakeArray[0].getCoordinateX() + 1 < fieldOBJ.getFieldSize():
                self.addNewHead(self._snakeArray[0].getCoordinateX() + 1, self._snakeArray[0].getCoordinateY(), fieldOBJ)
                # self._snakeArray[0].setCoordinateX(self._snakeArray[0].getCoordinateX() + 1)
            else:
                self.addNewHead(0, self._snakeArray[0].getCoordinateY(), fieldOBJ)
        # LEFT
        elif self._directionOfMovement == directions[3]:
            if 0 <= self._snakeArray[0].getCoordinateY() - 1:
                self.addNewHead(self._snakeArray[0].getCoordinateX(), self._snakeArray[0].getCoordinateY() - 1, fieldOBJ)
                # self._snakeArray[0].setCoordinateY(self._snakeArray[0].getCoordinateY() - 1)
            else:
                self.addNewHead(self._snakeArray[0].getCoordinateX(), fieldOBJ.getFieldSize() - 1, fieldOBJ)
                # self._snakeArray[0].setCoordinateY(fieldOBJ.getFieldSize() - 1)
        # RIGHT
        elif self._directionOfMovement == directions[4]:
            if self._snakeArray[0].getCoordinateY() + 1 < fieldOBJ.getFieldSize():
                self.addNewHead(self._snakeArray[0].getCoordinateX(), self._snakeArray[0].getCoordinateY() + 1, fieldOBJ)
                # self._snakeArray[0].setCoordinateY(self._snakeArray[0].getCoordinateY() + 1)
            else:
                self.addNewHead(self._snakeArray[0].getCoordinateX(), 0, fieldOBJ)
                # self._snakeArray[0].setCoordinateY(0)
        else:
            print("Invalid direction given!")

        self.setSnakeOnField(fieldOBJ)