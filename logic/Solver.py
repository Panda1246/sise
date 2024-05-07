from Board import Board

class Solver:
    def __init__(self, board):
        self.board = board

        self.solvedBoard = Board()
        self.solvedBoard.initializeWithBoard(board.getBoard())

    # To implement
    def solveBoardWithDFS(self):
        pass

    # To implement
    def solveBoardWithBFS(self):
        pass

    def solveBoardWithAStar(self):
        pass

    # Calculates Hamming metric to element with 0 for each part of puzzle
    # Returns number of puzzles that are in wrong places
    def getManhattanMatric(self) :
        tempBoard = Board.createSolvedBoard()

    # Calculates Manhattan metrics to element with 0 for each part of puzzle

    def getHammingMetric(self, currX, currY):
        pass


