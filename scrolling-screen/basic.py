from colorama import Back
from random import randint
from time import sleep

height = 50
width = 100
ground = 2*(height//3)

board = []

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
    num = randint(1, 8)
    if num == 1 and ground < height - 2:  # stop from going off bottom
        ground += 2
    elif num > 1 and num < 4 and ground < height - 1:  # stop from going off top
        ground += 1
    # between 4, 5, stay same
    elif num > 5 and num < 8 and ground > 3:  # keep a few away from top
        ground -= 1
    elif num == 8 and ground > 4:  # keep a few away from top
        ground -= 2

    for y in range(0, height):
        if y < ground:
            board[y].append(Back.BLACK + "  ")  # add new to end of line
        elif y == ground:
            board[y].append(Back.YELLOW + "  ")
        elif y > ground:
            board[y].append(Back.GREEN + "  ")

        # remove first item
        board[y].pop(0)

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


while True:
    draw()
    sleep(0.1)
