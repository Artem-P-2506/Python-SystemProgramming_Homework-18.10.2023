class Field:
    def __init__(self):
        self._fieldSize = 0
        self._field = self.__makeField()

    def getFieldSize(self):
        return self._fieldSize

    def __makeField(self):
        self._fieldSize = int(input("Введите размер поля (N*N): "))
        tempArray = []
        for i in range(self._fieldSize):
            tempArray.append([])
            for j in range(self._fieldSize):
                tempArray[i].append(".")
        return tempArray

    def _showField(self):
        print("\n=> ПОЛЕ:")
        for row in self._field:
            for column in row:
                print("\t\t", str(column), end="")
            print("\n")
    def getField(self):
        return self._field

    def deleteFromField(self, coordinateX, coordinateY):
        self._field[coordinateX][coordinateY] = "."

    # def setSnakeOnField(self, snakeOBJ):
    #     self._field[snakeOBJ.getCoordinateX()][snakeOBJ.getCoordinateY()] = snakeOBJ.getHeadSimbol()