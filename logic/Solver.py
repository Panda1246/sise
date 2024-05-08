from Board import Board

class Solver:
    def __init__(self, board):
        self.board = board
        self.solvedBoard = board.createSolvedBoard()
        self.boardX = board.getX()
        self.boardY = board.getY()


    # To implement
    def solveBoardWithDFS(self):
        pass

    # To implement
    def solveBoardWithBFS(self):
        pass

    def solveBoardWithAStar(self):
        pass

    # Calculates Hamming metric
    # Returns number of the puzzles that are in wrong places
    def getHammingMatric(self):
        missplacedValues = 0
        for i in range(0, self.boardY):
            for j in range(0, self.boardX):
                if self.board.getElement(j, i) != self.solvedBoard.getElement(j, i):
                    missplacedValues += 1
        return missplacedValues

    # Calculates Manhattan metrics to element with 0 for each part of puzzle
    def getManhattanMetric(self, currX, currY):
        pass


