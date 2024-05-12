import sys
from Solver import Solver
from Board import Board

board = Board()
board.initializeWithFile("testBoard.txt")
solver = Solver(board)

algorithm = ""

finalValues = solver.solveBoardWithAStar("hamm","DRLU") #solver.solveBoardWithAStar("hamm", "LRUD")
if finalValues is not None:
    solvedBoard = finalValues["solvedBoard"]
    moves = finalValues["moves"]
    executionTime = finalValues["executionTime"]
    visitedStates = finalValues["visitedStates"]
    processedStates = finalValues["processedStates"]
    maxDepth = finalValues["maxDepth"]
    print()
    print("solved board: " + str(solvedBoard))
    print("time: " + str(executionTime))
    print("moves: " + str(moves))
    print("visited states: " + str(visitedStates))
    print("processed states: " + str(processedStates))
    print("max depth: " + str(maxDepth))
    print()

    with open("result.txt", "w") as currFile:
        currFile.write("Time elapsed: " + str(executionTime) + "s\n")
        currFile.write("\nBoard to solve:\n " + str(board.getBoard()))
        currFile.write("\nSolved board: \n" + str(solvedBoard))


else:
    print("coultn't find value")

if algorithm == 'bfs':
    pass

elif algorithm == 'dfs':
    pass

elif algorithm == 'astar':
    pass