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

print(solver.getPossibleMoves())
solver.moveZeroElement('L')
#board.setElement(1, 2, 6)
board.printBoard()

solver.solveBoardWithBFS("LRUD")

if algorithm == 'bfs':
    pass

elif algorithm == 'dfs':
    pass

elif algorithm == 'astar':
    pass