class Point2D:
    def __init__(self, coordinateX, coordinateY):
        self._coordinateX = coordinateX
        self._coordinateY = coordinateY
        self._symbol = "NONE"

    def getCoordinateX(self):
        return int(self._coordinateX)

    def getCoordinateY(self):
        return int(self._coordinateY)

    def getSymbol(self):
        return str(self._symbol)

    def setCoordinateX(self, newCoordinateX):
        self._coordinateX = int(newCoordinateX)

    def setCoordinateY(self, newCoordinateY):
        self._coordinateY = int(newCoordinateY)

    def setSymbol(self, newSymbol):
        self._symbol = str(newSymbol)