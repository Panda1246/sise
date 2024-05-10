import copy
from collections import deque

from Board import Board
from time import time

class Solver:
    def __init__(self, board):
        self.board = board
        self.initialState = board.getBoard()
        self.solvedBoard = board.createSolvedBoard()
        self.boardX = board.getX()
        self.boardY = board.getY()
        self.boardQueue = deque()


    # To implement
    def solveBoardWithDFS(self):
        pass

    # To implement
    def solveBoardWithBFS(self, searchingMethod):
        solved = False
        visitedStates = 0
        processedStates = 0
        maxDepth = 0
        startTime = time()
        visitedBoards = list()
        self.boardQueue.appendleft([self.board.getBoard(), self.board.getBoard()])
        visitedBoards.append(self.board.getBoard())

        while self.boardQueue and not solved:
            currentIteration = self.boardQueue.pop()
            currentBoard = currentIteration[0]
            parent = currentIteration[1]
            parentForThisIteration = copy.deepcopy(currentBoard)

            tempBoard = Board()
            tempBoard.initializeWithBoard(currentBoard)
            currentMoves = self.getPossibleMoves(tempBoard)

            for letter in searchingMethod:
                if letter in currentMoves:
                    tempBoard = Board()
                    tempBoard.initializeWithBoard(currentBoard)
                    self.moveZeroElement(letter, tempBoard)


                    if tempBoard.getBoard() not in parentForThisIteration:
                        visitedBoards.append(tempBoard.getBoard())
                        self.boardQueue.appendleft([tempBoard.getBoard(), parentForThisIteration])


                    # solved, we have the right board
                    if tempBoard.getBoard() == self.solvedBoard.getBoard():
                        self.board = tempBoard
                        solved = True
                        break



                    #print("ok")
        print("the end")



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
    def getPossibleMoves(self, currBoard: Board):
        allPossibleMoves = ["L", "R", "U", "D"]
        zeroElementPosition = currBoard.getEmptyPosition()
        currX = zeroElementPosition[0]
        currY = zeroElementPosition[1]
        if currY == 0:
            allPossibleMoves.remove("U")

        if currY == currBoard.getY() - 1:
            allPossibleMoves.remove("D")

        if currX == 0:
            allPossibleMoves.remove("L")

        if currX == currBoard.getX() - 1:
            allPossibleMoves.remove("R")

        return allPossibleMoves

    def moveZeroElement(self, direction: str, currBoard: Board):
        try:
            currZeroPosition = currBoard.getEmptyPosition()
            currZeroX = currZeroPosition[0]
            currZeroY = currZeroPosition[1]
            if direction == 'L':
                tempValue = currBoard.getElement(currZeroX - 1, currZeroY)
                currBoard.setElement(currZeroX, currZeroY, tempValue)
                currBoard.setElement(currZeroX - 1, currZeroY, 0)

            elif direction == 'R':
                tempValue = currBoard.getElement(currZeroX + 1, currZeroY)
                currBoard.setElement(currZeroX, currZeroY, tempValue)
                currBoard.setElement(currZeroX + 1, currZeroY, 0)

            elif direction == "U":
                tempValue = currBoard.getElement(currZeroX, currZeroY - 1)
                currBoard.setElement(currZeroX, currZeroY, tempValue)
                currBoard.setElement(currZeroX, currZeroY - 1, 0)

            elif direction == "D":
                tempValue = currBoard.getElement(currZeroX, currZeroY + 1)
                currBoard.setElement(currZeroX, currZeroY, tempValue)
                currBoard.setElement(currZeroX, currZeroY + 1, 0)

        except IndexError:
            print("Wrong index!!!")





