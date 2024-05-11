import sys
from Solver import Solver
from Board import Board

board = Board()


board.initializeWithFile("testBoard.txt")
board.printBoard()
solver = Solver(board)

newBoard = board.createSolvedBoard()

print()

newBoard.printBoard()
print()
x = solver.getHammingMatric()
print(x)

algorithm = sys.argv[0]

#print(solver.getPossibleMoves(solver.))
#solver.moveZeroElement('L')
#board.setElement(1, 2, 6)
initialBoard = Board()
initialBoard.initializeWithBoard(board.getBoard())

if initialBoard.getBoard() == board.getBoard():
    print("ok!!!")


finalValues = solver.solveBoardWithDFS("LRUD")
solvedBoard = finalValues[0]
time = finalValues[1]

with open("result.txt", "w") as currFile:
    currFile.write("Time elapsed: " + str(time))
    currFile.write("\nBoard to solve:\n " + str(board.getBoard()))
    currFile.write("\nSolved board: \n" + str(solvedBoard.getBoard()))

initialBoard.printBoard()
print('------------')
solvedBoard.printBoard()

if algorithm == 'bfs':
    pass

elif algorithm == 'dfs':
    pass

elif algorithm == 'astar':
    pass