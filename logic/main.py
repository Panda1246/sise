import sys
from Solver import Solver
from Board import Board

board = Board()


board.initializeWithFile("testBoard.txt")
board.printBoard()
solver = Solver(board)

testBoard = board.createSolvedBoard()
newBoard = Board()
print()

newBoard.initializeWithBoard(testBoard)
newBoard.printBoard()

algorithm = sys.argv[0]

if algorithm == 'bfs':
    pass

elif algorithm == 'dfs':
    pass

elif algorithm == 'astr':
    pass