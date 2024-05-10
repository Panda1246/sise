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


solvedBoard = solver.solveBoardWithBFS("LRUD")
initialBoard.printBoard()
print('------------')
solvedBoard.printBoard()

if algorithm == 'bfs':
    pass

elif algorithm == 'dfs':
    pass

elif algorithm == 'astar':
    pass