from random import *
from solver import *

def genPuzzle():
    board = [[0] * 9 for _ in range(9)]
    clues = randint(17,27)
    for _ in range(clues):
        i = randint(0,8)
        j = randint(0,8)
        while board[i][j] != 0:
            i = randint(0,8)
            j = randint(0,8)
        num = randint(1,9)
        while not isValid(num, i, j, board):
            num = randint(1,9)
        board[i][j] = num
    return board
