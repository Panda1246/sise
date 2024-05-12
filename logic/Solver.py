import copy
from collections import deque
from queue import PriorityQueue

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
            processedStates += 1
            noMoreOptions = True
            currState, currMoves, depth = self.boardStack.popleft()
            # print(str(currState)+  " " + str(depth))
            if currState == self.solvedBoard.getBoard():
                stopTime = time()
                tempBoard.initializeWithBoard(currState)
                finalMovesStr = ""
                for letter in currMoves:
                    finalMovesStr += letter

                return {"solvedBoard": tempBoard.getBoard(),
                        "moves": finalMovesStr,
                        "executionTime": round((stopTime - startTime) * 1000, 3),
                        "visitedStates": visitedStates,
                        "processedStates": processedStates,
                        "maxDepth": maxDepth}

            self.boardStack.appendleft([currState, currMoves, depth])
            tempBoard.initializeWithBoard(currState)
            possibleMoves = self.getPossibleMoves(tempBoard)
            if depth <= 20:
                if depth > maxDepth:
                    maxDepth = depth
                for letter in searchingOrder:
                    if letter in possibleMoves:
                        tempBoard.initializeWithBoard(currState)
                        self.moveZeroElement(letter, tempBoard)
                        #  VERY IMPORTANT!!!!
                        #  DEPTH NEED TO BE ADDED HERE , NOT IN THE CODE BELOW TO AVOID DEADLOCK(or something similar)
                        depth += 1

                        if tuple(map(tuple, tempBoard.getBoard())) not in visitedBoards or depth < visitedBoards[
                            tuple(map(tuple, tempBoard.getBoard()))]:
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
                            visitedStates += 1
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
        self.boardQueue.appendleft([self.board.getBoard(), self.board.getBoard(), ""])
        visitedBoards.append(self.board.getBoard())

        while self.boardQueue and not solved:
            processedStates += 1

            currentIteration = self.boardQueue.pop()
            currentBoard = currentIteration[0]
            parent = currentIteration[1]
            currentMoveOrder = currentIteration[2]

            parentForThisIteration = copy.deepcopy(currentBoard)

            tempBoard = Board()
            tempBoard.initializeWithBoard(currentBoard)
            currentMoves = self.getPossibleMoves(tempBoard)
            currDepth += 1
            if currDepth > maxDepth:
                maxDepth = currDepth
            print("curr depth: " + str(currDepth))
            for letter in searchingOrder:
                if letter in currentMoves:
                    tempBoard = Board()
                    tempBoard.initializeWithBoard(currentBoard)
                    self.moveZeroElement(letter, tempBoard)

                    if tempBoard.getBoard() != parent or tempBoard.getBoard() not in visitedBoards:
                        visitedStates += 1
                        visitedBoards.append(tempBoard.getBoard())
                        currentMoveOrder += letter
                        self.boardQueue.appendleft([tempBoard.getBoard(), parentForThisIteration, currentMoveOrder])

                    # solved, we have the right board
                    if tempBoard.getBoard() == self.solvedBoard.getBoard():
                        print("solved")
                        tempBoard.printBoard()
                        stopTime = time()
                        finalTime = stopTime - startTime
                        print("Time elapsed: " + str(finalTime) + " s")
                        return {"solvedBoard": tempBoard.getBoard(),
                                "moves": currentMoveOrder,
                                "executionTime": round((stopTime - startTime) * 10000, 3),
                                "visitedStates": visitedStates,
                                "processedStates": processedStates,
                                "maxDepth": maxDepth}

                    # print("ok")
        print("the end")

    def solveBoardWithAStar(self, heuristic, searchingOrder):
        if heuristic == "hamm":
            calculateH = self.getHammingMatric
        elif heuristic == "manh":
            calculateH = self.getManhattanMetric

        startTime = time()
        priorityQueue = PriorityQueue()
        visitedBoards = {}

        # Initialize the priority queue with the initial state
        priorityQueue.put((calculateH(self.board), [self.board.getBoard(), "", 0]))
        visitedBoards[tuple(map(tuple, self.board.getBoard()))] = 0
        processedStates, visitedStates, maxDepth = 0, 0, 0

        while not priorityQueue.empty():
            currPriority, (currBoardState, currLettersOrder, currDepth) = priorityQueue.get()
            processedStates += 1
            if currDepth > maxDepth:
                maxDepth = currDepth
            if currBoardState == self.solvedBoard.getBoard():
                stopTime = time()
                tempBoard = Board()
                tempBoard.initializeWithBoard(currBoardState)
                return {"solvedBoard": tempBoard.getBoard(),
                        "moves": currLettersOrder,
                        "executionTime": round((stopTime - startTime) * 1000, 3),
                        "visitedStates": visitedStates,
                        "processedStates": processedStates,
                        "maxDepth": maxDepth}

            tempBoard = Board()
            tempBoard.initializeWithBoard(currBoardState)
            currentMoves = self.getPossibleMoves(tempBoard)

            for letter in searchingOrder:
                if letter in currentMoves:
                    tempBoard = Board()
                    tempBoard.initializeWithBoard(currBoardState)
                    self.moveZeroElement(letter, tempBoard)

                    # Calculate the new cost
                    # f(n) = g(n) + h(n)
                    newCost = currDepth + 1 + calculateH(tempBoard)

                    if tuple(map(tuple, tempBoard.getBoard())) not in visitedBoards:
                        visitedStates += 1
                        visitedBoards[tuple(map(tuple, tempBoard.getBoard()))] = newCost
                        priorityQueue.put((newCost, [tempBoard.getBoard(), currLettersOrder + letter, currDepth + 1]))

        return None

    # Calculates Hamming metric
    # Returns number of the puzzles that are in wrong places
    def getHammingMatric(self, board):
        missplacedValues = 0
        for i in range(0, self.boardY):
            for j in range(0, self.boardX):
                if board.getElement(j, i) != self.solvedBoard.getElement(j, i) and board.getElement(j, i) != 0:
                    missplacedValues += 1
        return missplacedValues

    # Calculates Manhattan metrics to element with 0 for each part of the puzzle
    def getManhattanMetric(self, board):
        finalValue = 0
        for i in range(self.boardY):
            for j in range(self.boardX):
                currValue = board.getElement(j, i)
                if currValue != 0:
                    currX = j
                    currY = i
                    targetY, targetX = self.solvedBoard.getElementPosition(currValue)
                    finalValue += abs(currY - targetY) + abs(currX - targetX)
        return finalValue

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
