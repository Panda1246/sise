import copy

class Board:
    def __init__(self):
        self.boardData = []
        self.x = 0
        self.y = 0
        self.emptyPosition = [None, None]
        self.listOfStates = []

    # w pliku pierwsza linijka musi zawierac wymiary ukladanki (x y)
    # kolejne linie sa odwzorowaniem rozmieszczenia elementow na ukladance
    # 0 to element pusty
    # przykladowa ukladanka 3x3:
    '''
    3 3
    1 0 2
    3 4 5
    6 7 8
    '''

    def initializeWithFile(self, fileName):
        with open(fileName, 'r') as currFile:
            matrixSize = currFile.readline().strip().split()
            self.x = int(matrixSize[0])
            self.y = int(matrixSize[1])

            #inicializacja pustej 2-wymiarowej tablicy
            self.boardData = self.createEmpty2DArray(self.x, self.y)
            print(str(self.x) + " " + str(self.y))
            for i in range(0, self.y):
                currLine = currFile.readline().strip().split()
                for j in range(0, self.x):
                    self.boardData[i][j] = int(currLine[j])
                    if self.boardData[i][j] == 0:
                        # zapisanie pustej pozycji
                        self.emptyPosition = [i, j]

    def initializeWithBoard(self, board):
        self.boardData = board
        self.y = len(self.boardData)
        self.x = len(self.boardData[0])
        self.emptyPosition = self.getEmptyPosition()

    def printBoard(self):
        for i in range(0, self.y):
            for j in range(0, self.x):
                print(str(self.boardData[i][j]), end=" ")
            print()

    def createSolvedBoard(self):
        tempBoard = Board()
        newBoard = self.createEmpty2DArray(self.x, self.y)
        for i in range(0, self.y):
            for j in range(0, self.x):
                if i == self.y - 1 and j == self.x - 1:
                    # ostatni element jest zawesze zerem
                    newBoard[i][j] = 0
                else:
                    newBoard[i][j] = self.y * i + j + 1
        tempBoard.initializeWithBoard(newBoard)
        return tempBoard


    def createEmpty2DArray(self, x, y):
        return [[None] * self.y for _ in range(self.x)]

    def getEmptyPosition(self):
        for i in range(0, self.x):
            for j in range(0, self.y):
                if self.boardData[i][j] == 0:
                    return [j, i]

    def getElement(self, x, y):
        return self.boardData[y][x]

    def setElement(self, x, y, value):
        self.boardData[y][x] = value

    def getBoard(self):
        return copy.deepcopy(self.boardData)

    def getX(self):
        return copy.deepcopy(self.x)

    def getY(self):
        return copy.deepcopy(self.y)
    def updateStates(self, states):
        self.listOfStates = states

    def getStates(self):
        return copy.deepcopy(self.listOfStates)