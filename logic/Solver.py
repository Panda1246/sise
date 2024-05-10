from collections import deque

from Board import Board
from time import time

class Solver:
    def __init__(self, board):
        self.board = board
        self.solvedBoard = board.createSolvedBoard()
        self.boardX = board.getX()
        self.boardY = board.getY()
        self.boardQueue = deque()


    # To implement
    def solveBoardWithDFS(self):
        pass

    # To implement
    def solveBoardWithBFS(self, searchingMethod):
        visitedStates = 0
        processedStates = 0
        maxDepth = 0
        startTime = time()
        visitedBoards = []
        self.boardQueue.appendleft(self.board.getBoard())
        while self.board.getBoard() != self.solvedBoard:
            currentMoves = self.getPossibleMoves()
            for letter in searchingMethod:
                if letter in currentMoves:
                    tempBoard = Board()
                    currentBoard = self.boardQueue.pop()
                    tempBoard.initializeWithBoard(currentBoard)
                    print("ok")




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

    # possible moves for 0 element in the board
    def getPossibleMoves(self):
        allPossibleMoves = ["L", "R", "U", "D"]
        zeroElementPosition = self.board.getEmptyPosition()
        currX = zeroElementPosition[0]
        currY = zeroElementPosition[1]
        if currY == 0:
            allPossibleMoves.remove("U")

        if currY == self.boardY - 1:
            allPossibleMoves.remove("D")

        if currX == 0:
            allPossibleMoves.remove("L")

        if currX == self.boardX - 1:
            allPossibleMoves.remove("R")

        return allPossibleMoves

    def moveZeroElement(self, direction):
        try:
            currZeroPosition = self.board.getEmptyPosition()
            currZeroX = currZeroPosition[0]
            currZeroY = currZeroPosition[1]
            if direction == 'L':
                tempValue = self.board.getElement(currZeroX - 1, currZeroY)
                self.board.setElement(currZeroX, currZeroY, tempValue)
                self.board.setElement(currZeroX - 1, currZeroY, 0)

            elif direction == 'R':
                tempValue = self.board.getElement(currZeroX + 1, currZeroY)
                self.board.setElement(currZeroX, currZeroY, tempValue)
                self.board.setElement(currZeroX + 1, currZeroY, 0)

            elif direction == "U":
                tempValue = self.board.getElement(currZeroX, currZeroY - 1)
                self.board.setElement(currZeroX, currZeroY, tempValue)
                self.board.setElement(currZeroX, currZeroY - 1, 0)

            elif direction == "D":
                tempValue = self.board.getElement(currZeroX, currZeroY + 1)
                self.board.setElement(currZeroX, currZeroY, tempValue)
                self.board.setElement(currZeroX, currZeroY + 1, 0)

        except IndexError:
            print("Wrong index!!!")





