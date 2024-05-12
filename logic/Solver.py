import copy
from collections import deque

from Board import Board
from time import time, sleep


class Solver:
    def __init__(self, board):
        self.board = board
        self.initialState = board.getBoard()
        self.solvedBoard = board.createSolvedBoard()
        self.boardX = board.getX()
        self.boardY = board.getY()
        self.boardQueue = deque()
        self.boardStack = deque()

    # To implement
    def solveBoardWithDFS(self, searchingOrder):
        # reversing searching order to encure valid order in the stack implementation
        # searchingOrder = searchingOrder[::-1]

        solved = False
        visitedStates = 0
        processedStates = 0
        maxDepth = 0
        currDepth = 0
        startTime = time()

        visitedBoards = {}

        # for now this is board stack
        # stack initialization with board state and moves, depth
        self.boardStack.appendleft([self.board.getBoard(), [], 0])
        b = self.board.getBoard()
        visitedBoards[tuple(map(tuple, self.board.getBoard()))] = 0
        tempBoard = Board()

        while self.boardStack:
            noMoreOptions = True
            currState, currMoves, depth = self.boardStack.popleft()
            # print(str(currState)+  " " + str(depth))
            if currState == self.solvedBoard.getBoard():
                stopTime = time()
                tempBoard.initializeWithBoard(currState)
                return [tempBoard, stopTime - startTime]

            self.boardStack.appendleft([currState, currMoves, depth])
            tempBoard.initializeWithBoard(currState)
            possibleMoves = self.getPossibleMoves(tempBoard)
            if depth < 20:
                for letter in searchingOrder:
                    if letter in possibleMoves:
                        tempBoard.initializeWithBoard(currState)
                        self.moveZeroElement(letter, tempBoard)
                        visitedStates += 1

                        #  VERY IMPORTANT!!!!
                        #  DEPTH NEED TO BE ADDED HERE , NOT IN THE CODE BELOW TO AVOID DEADLOCK(or something similar)
                        depth += 1

                        if tuple(map(tuple, tempBoard.getBoard())) not in visitedBoards or depth < visitedBoards[tuple(map(tuple, tempBoard.getBoard()))]:
                            if tuple(map(tuple, tempBoard.getBoard())) in visitedBoards:
                                if depth < visitedBoards[tuple(map(tuple, tempBoard.getBoard()))]:
                                    #pass
                                    print("visited")

                            print("depth " + str(depth))
                            visitedBoards[tuple(map(tuple, tempBoard.getBoard()))] = depth
                            currMoves.append(letter)
                            self.boardStack.appendleft([copy.deepcopy(tempBoard.getBoard()), copy.deepcopy(currMoves),
                                                        copy.deepcopy(depth)])
                            noMoreOptions = False
                            break

                if noMoreOptions is True:
                    self.boardStack.popleft()
            else:
                self.boardStack.popleft()

    # To implement
    def solveBoardWithBFS(self, searchingOrder):
        solved = False
        visitedStates = 0
        processedStates = 0
        maxDepth = 0
        startTime = time()
        visitedBoards = list()
        currDepth = 0
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
            currDepth += 1
            print("curr depth: " + str(currDepth))
            for letter in searchingOrder:
                if letter in currentMoves:
                    tempBoard = Board()
                    tempBoard.initializeWithBoard(currentBoard)
                    self.moveZeroElement(letter, tempBoard)

                    if tempBoard.getBoard() != parent or tempBoard.getBoard() not in visitedBoards:
                        visitedBoards.append(tempBoard.getBoard())
                        self.boardQueue.appendleft([tempBoard.getBoard(), parentForThisIteration])

                    # solved, we have the right board
                    if tempBoard.getBoard() == self.solvedBoard.getBoard():
                        print("solved")
                        tempBoard.printBoard()
                        stop = time()
                        finalTime = stop - startTime
                        print("Time elapsed: " + str(finalTime) + " s")
                        return [tempBoard, finalTime]

                    # print("ok")
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

    # Calculates Manhattan metrics to element with 0 for each part of the puzzle
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
