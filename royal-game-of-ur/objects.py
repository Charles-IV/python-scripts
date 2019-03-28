# The Royal Game of Ur
# objects.py

from functions import *  # import all useful functions
from random import getrandbits


class piece:
    def __init__(self, player):
        self.player = player  # 1 or 2 depending on player 1 or 2
        self.pos = 0  # int from 1 to 20 showing place on board. 0 is waiting or knocked off, -1 is home


class player:
    def __init__(self, no):
        self.no = no  # player number - 1 or 2 depending on player 1 or 2
        self.hand = []  # players hand of pieces - TODO: is piece.player obsolete now?

    
    def roll(self):  # function to roll and start move
        whites = 0  # number of white sides up that have been rolled

        for i in range(4):  # roll for dices
            if bool(getrandbits(1)):  # true = white, false = black (1/2 probability for both)
                whites += 1

        print("Player {} rolled {} whites!".format(self.no, whites))

        # oh boy choosing moves is gonna be hell


