from colorama import Back
from random import randint
from time import sleep
from keyboard import is_pressed

height = 20
width = 20
ground = 2*(height//3)
hold = 0.5  # time to sleep for

board = []


class Player:
    def __init__(self):
        self.yPos = ground - 2  # start in middle of tunnel

    def up(self, inp):
        if inp == "up":
            self.yPos -= 1
        elif inp == "down":
            self.yPos += 1
        #inp = "null"  # reset to go straight  # TODO: do in while true


for y in range(0, height):
    board.append([])
    for x in range(0, width + 5):  # 5 buffer
        """
        if y < ground:  # if top two thirds
            board[y].append(Back.BLACK + "  ")
        elif y == ground:
            board[y].append(Back.YELLOW + "  ")
        elif y > ground:
            board[y].append(Back.GREEN + "  ")
            """
        board[y].append(Back.RESET + "  ")

print("\033[2J \033[H")  # clear screen


def up():
    global ground # shutup its bad practice, i just wanna see if this works
    num = randint(1, 16)
    if num == 1 and ground < height - 2:  # stop from going off bottom
        ground += 2
    elif num > 1 and num < 5 and ground < height - 1:  # stop from going off top
        ground += 1
    # between 4, 5, stay same
    elif num > 10 and num < 16 and ground > 9:  # keep a few away from top
        ground -= 1
    elif num == 16 and ground > 10:  # keep a few away from top
        ground -= 2

    for y in range(0, height):
        if y < ground - 6:
            board[y].append(Back.GREEN + "  ")
        elif y == ground - 6:
            board[y].append(Back.YELLOW + "  ")
        elif y < ground:  # bits above should have already been caught
            board[y].append(Back.BLACK + "  ")  # add new to end of line
        elif y == ground:
            board[y].append(Back.YELLOW + "  ")
        elif y > ground:
            board[y].append(Back.GREEN + "  ")

        # remove first item
        board[y].pop(0)

    # TODO: clear old positions of player
    if board[p.yPos][4] == Back.BLACK + "  " or board[p.yPos][4] == Back.RESET + "  " :  # if in clear space
        board[p.yPos][4] = Back.RED + "  "
    else:  # if in ground
        print("GAME OVER\n\n\n\n\n\n\n")
        input()

    return board  # return new board


def draw():
    global board  # shutup its bad practice, i just wanna see if this works
    # create old board to compare new board
    oldBoard = []
    for row in range(0, height):
        oldBoard.append([])
        for item in range(0, width):
            oldBoard[row].append(board[row][item])  # only copy literals to avoid pythons stupid linking

    # update board and console
    board = up()  # update new board

    console = ""

    # draw snake and food, update board
    for y in range(1, height+1):
        # go across screen
        for x in range(1, width+1):
            if board[y-1][x-1] != oldBoard[y-1][x-1]:  # if the colour of this position has changed
                console += "\033[{};{}H{}".format(y+2, ((x+2)*2)-1, board[y-1][x-1])  # log position as to be overwritten

    print(console)  # update screen


count = 0  # running count of frame we're on
inp = "null"
p = Player()

while True:
    if is_pressed("up"):
        inp = "up"
    elif is_pressed("down"):
        inp = "down"

    p.up(inp)
    inp = "null"

    draw()
    sleep(hold)
    count += 1  # increment counter
    if (count % 10) == 0:  # every 100
        hold -= 0.01
