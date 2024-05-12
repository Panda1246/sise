import sys
from Solver import Solver
from Board import Board

board = Board()
'''board.initializeWithFile("testBoard.txt")
solver = Solver(board)
'''

# program bfs RDUL 4x4_01_0001.txt 4x4_01_0001_bfs_rdul_sol.txt 4x4_01_0001_bfs_rdul_stats.txt

algorithm = sys.argv[1]
boardSourceFile = sys.argv[3]
solDestFile = sys.argv[4]
statsDestFile = sys.argv[5]

board.initializeWithFile(boardSourceFile)
solver = Solver(board)

solved = None

if algorithm == "bfs":
    searchingOrder = sys.argv[2]
    solved = solver.solveBoardWithBFS(searchingOrder)

elif algorithm == "dfs":
    searchingOrder = sys.argv[2]
    solved = solver.solveBoardWithDFS(searchingOrder)

elif algorithm == "astr":
    heuristic = sys.argv[2]
    solved = solver.solveBoardWithAStar(heuristic)


solutionMoves = solved["moves"]
solutionLen = len(solutionMoves)
visitedStates = solved["visitedStates"]
processedStates = solved["processedStates"]
maxDepth = solved["maxDepth"]
processingTime = solved["executionTime"]

with open(solDestFile, "w") as solutionDestinationFile, open(statsDestFile, "w") as statisticsDestinationFile:
    solutionDestinationFile.write(str(solutionLen) + '\n')
    solutionDestinationFile.write(str(solutionMoves)+ '\n')
    statisticsDestinationFile.write(str(solutionLen)+ '\n')
    statisticsDestinationFile.write(str(visitedStates)+ '\n')
    statisticsDestinationFile.write(str(processedStates)+ '\n')
    statisticsDestinationFile.write(str(maxDepth)+ '\n')
    statisticsDestinationFile.write(str(processingTime)+ '\n')

'''algorithm = ""

finalValues = solver.solveBoardWithDFS("DRLU") #solver.solveBoardWithAStar("hamm", "LRUD")
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
    pass'''