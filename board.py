import numpy as np


def create_board():
    board= np.zeros((6,7))
    return board

board = create_board()
game_over = False
turn = 0

while not game_over:
    if turn == 0:
        selection = int(input("player 1 make your selection: "))
    else:
        selection = int(input("player 2 make your selection: "))
    turn+=1


    turn = turn %2

