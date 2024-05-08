from collections import deque

from Board import Board
from time import time

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
        visited_states = 0
        processed_states = 0
        max_depth = 0
        start_time = time()

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

    def getPossibleMoves(self, currX, currY):
        allPossibleMoves = ["L", "R", "U", "D"]
        if currY == 0:
            allPossibleMoves.remove("U")

        if currY == self.boardY - 1:
            allPossibleMoves.remove("D")

        if currX == 0:
            allPossibleMoves.remove("L")

        if currX == self.boardX - 1:
            allPossibleMoves.remove("R")

        return allPossibleMoves



