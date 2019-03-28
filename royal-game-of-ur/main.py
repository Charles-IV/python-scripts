# The Royal Game of Ur
# main.py

from objects import player, piece
from functions import *  # import all useful functions
from os import system  # for ansi codes at school

system('')  # run empty command to enable ansi codes at school

# initialise variables
won = False

def gen(player):  # generate pieces for player
    for i in range(7):  # 7 pieces per player
        player.hand.append(piece(player.no))


def draw(board):  # draw board - TODO: may need players hands instead?
    print("lmao cant draw yet")  # TODO: replace when you can


def gameOverCheck(p1, p2):  # check if game over
    # check if player 1 has won
    home = 0  # number of pieces player has brought home
    for piece in p1.hand:  # iterate through player 1's hand
        if piece.pos == -1:  # if piece is home
            home += 1
    
    if home == 7:  # if player has all 7 pieces home
        return 1  # return 1 for 'player 1 has won'

    # TODO: maybe change this so it only checks one player at a time?

    


def main():  # main starting function
    cls()  # clear the screen
    # generate player 1
    player1 = player(1)
    # generate player 2
    player2 = player(2)

    # generate pieces for player 1
    gen(player1)
    # generate pieces for player 2
    gen(player2)

    while not won:
        cls()
        print("boopety boop another round")  # TODO: remove this


main()

