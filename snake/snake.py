#!/usr/bin/python3

import os, random
from time import time
from keyboard import is_pressed
from colorama import init, Fore, Back, Style

init()  # for windows

# some vars

width = 20
height = 20
fps = 10
epilepsy = -1 # traust me, you don't want to enable this
              # (-1 for disabled, 0 for colour set 1, 1 for colour set 2)

# colours for snake, border, food, and background
dispCols = [Back.GREEN, Back.WHITE, Back.RED, Back.RESET]


###########
# CLASSES #
###########

class Food:
    def __init__(self):
        self.up()  # generate values


    def up(self):  # only run when needed
        self.xPos = random.randint(1, width)
        self.yPos = random.randint(1, height)
        self.pos = str(self.xPos) + "x" + str(self.yPos)  # makes comparing easier
        try:
            for part in v.snake:
                if part.pos == self.pos:  # if the snake is where the food just spawned
                    # TODO: sometimes the food doesn't detect that it is where the snake already is, but most of the time it does
                    self.up()  # try to change food postition to where the snake isn't
        except NameError:  # if variables haven't been inited yet
            if self.pos == str(width//2)+"x"+str(height//2):  # make sure to not spawn at snake spawn point
                self.up()


class SnakeHead:
    def __init__(self):
        self.xPos = width // 2
        self.yPos = height // 2
        self.dir = "d"  # wasd - starts going right
        self.pos = str(self.xPos) + "x" + str(self.yPos)
        self.oldPos = self.pos  # so parts can follow
        self.over = False  # have a variable for this so gaveOver gan be called and the full snake array passed to it, rather than passing it needlessly through the up method.


    def up(self):
        # get direction
        self.dir = v.inp  # TODO: make this more efficient, don't need duplicate variables
                          # currently I'm using this to compare the current direction to the input, so the player doesn't turn 180 and kill themselves, but it could be made more efficient

        # move
        if self.dir == "w":  # if up
            self.yPos -= 1
        elif self.dir == "a":  # if left
            self.xPos -= 1
        elif self.dir == "s":  # if down
            self.yPos += 1
        elif self.dir == "d":  # if right
            self.xPos += 1

        # update old position
        self.oldPos = self.pos
        # update current position
        self.pos = str(self.xPos) + "x" + str(self.yPos)

        # check if colliding with something
        if self.pos == v.food.pos:  # if eating some food
            spawnPart(v.snake)  # add a part to the snake
            v.score += 1  # increment score
            v.food.up()  # respawn food

        if (1 > self.xPos or self.xPos > width) or (1 > self.yPos or self.yPos > height):  # if off screen
            gameOver()  # call game over screen and reset vars

        for part in v.snake[1:]:  # iterate through the parts on the snake, skipping the head
            if part.pos == self.pos:  # if you're eating yourself
                gameOver()


class SnakePart:
    def __init__(self, mummy):
        self.parent = mummy  # mummy!
        self.pos = self.parent.oldPos  # set position to mummys old possition
        self.up()  # create other variables

    def up(self):
        # update old position
        self.oldPos = self.pos
        # update current possition to parents old position and update xPos and yPos
        self.pos = self.parent.oldPos
        self.xPos, self.yPos = self.pos.split("x")
        self.xPos = int(self.xPos)  # change to integers
        self.yPos = int(self.yPos)


class runtimeVars:  # object for storing runtime variables
    def __init__(self):
        # get highscore - not reset every time so put here
        try:
            f = open("highscore.txt", "r")  # try to open as read
        except IOError:  # if the file doesn't exist
            f = open("highscore.txt", "w")  # create file
            f.write("0")  # write 0, it will be replaced with score later
            f.close()
            f = open("highscore.txt", "r")  # now open as read

        self.highscore = f.read()  # read highscore
        f.close()  # close file

        self.reset()  # generate other variables

    def reset(self):  # reset all to 0
        self.snake = []
        self.food = Food()
        self.snake.append(SnakeHead())
        for i in range(0, 5):  # create 5 parts
            self.snake = spawnPart(self.snake)
        self.inp = "d"

        self.score = 0

        self.bordersDrawn = False

        # board to only print updates
        self.board = []
        for row in range(0, height):
            self.board.append([])
            for column in range(0, width):
                self.board[row].append(Back.RESET)  # background is probably transparent

    def resetBoard(self):
        cls()  # clear screen

        self.bordersDrawn = False  # borders have been cleared

        # clear the board as it has been wiped
        self.board = []
        for row in range(0, height):
            self.board.append([])
            for column in range(0, width):
                self.board[row].append(Back.RESET)  # background is probably transparent


############
# FUNTIONS #
############

# functions called depending on what happens what happens in game
def gameOver():
    cls()
    # check highscore
    if v.score > int(v.highscore):  # if new highscore
        v.highscore = str(v.score)  # replace old one
        f = open("highscore.txt", "w")
        f.write(v.highscore)
        f.close()

    print("\n\n"+
        "      _____          __  __ ______    ______      ________ _____  \n"+
        "     / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \ \n"+
        "    | |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) |\n"+
        "    | | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  / \n"+
        "    | |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \ \n"+
        "     \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_\ \n\n"+
        "   Y O U   D I E D\n\n"+
        "   Score = {}\n".format(v.score)+
        "   Highscore = {}\n\n".format(v.highscore))
    input("   >")  # clear out all the gunk waiting to be inputed so I get y or n next
    print("\033[1A   Do you want to restart? [Y/n]: ", end="")  # ansi escape to go up one line to overwrite last line
    restart = input()
    if restart.lower() == "n":
        exit()
    v.reset()  # reset all variables
    cls()  # clear screen do this isn't left over later
    # else just return


def pause():
    for y in range((height//4)+3, (3*(height//4))+3):  # print from a quater to three quarters down the board
        print("\033[{0};{2}H{1}\033[{0};{3}H{1}".format(y, Back.WHITE+"   ", width-(width//4)+4, width+(width//4)+4)+Back.RESET, end="")
        # print two white lines parallel to each other

    print("\033["+str(height+5)+";4HP A U S E D        (press enter to play)", end="")
    input()  # wait until enter is pressed

    # just clear whole screen because rounding is a problem
    v.resetBoard()

# colour customisation functions
def validateColInput(disp, col):
    colours = [Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE, Back.RESET]  # available colours
    if col == "":  # if no input (default)
        return True  # dont change value
    try:
        col = int(col)  # see if it can be casted as integer
        if col < 1 or col > 9:  # if input out of range
            raise Exception()
    except (ValueError, Exception):
        print("     Please enter a number between 1 and 9 (inclusive) or press enter for default")
        return False

    # we now know the input is valid
    dispCols[disp] = colours[col-1]  # change colour to display
    return True  # tell customise() it's valid


def getCol(arr):
    colours = [Back.BLACK+"1. black", Back.RED+"2. red", Back.GREEN+"3. green", Back.YELLOW+"4. yellow", Back.BLUE+"5. blue", Back.MAGENTA+"6. magenta", Back.CYAN+"7. cyan", Back.WHITE+"8. white", Back.RESET+"9. none", Back.RESET]
    cls()
    print(Back.RESET)
    print("\n\n   Colour for {}:\n".format(arr[0])+
    "   {0}{9}\n   {1}{9}\n   {2}{9}\n   {3}{9}\n   {4}{9}\n   {5}{9}\n   {6}{9}\n   {7}{9}\n   {8}{9}".format(*colours)
    )

    valid = False
    while not valid:
        col = input("\n   Enter number colour for {} (default {}): ".format(arr[0], arr[1]))
        valid = validateColInput(arr[2], col)


def customise():  # allow the user to change the colour of the parts
    cls()

    cust = [  # array of customisable parts. "name", default, possition in dispCols
        ["snake", 3, 0],
        ["border", 8, 1],
        ["food", 2, 2],
        ["background", 9, 3]
    ]

    for i in cust:
        getCol(i)

    cls()
    print(Back.RESET)
    print("   Success!")

    for i in range(0, len(cust)):
        print("   Colour for {}: {}".format(cust[i][0], dispCols[i]+"  "+Back.RESET))

    input("\n   (continue)\n")


# functions to assist with repetative tasks
def cls():  # to clear screen
    print("\033[2J \033[H", end="")  # clear screen and go to 0,0, then go to 0,0 again because ansi sucks? There's a problem with Esc[2J
    # This method works when access to command prompt is blocked


def spawnPart(snake):
    snake.append(SnakePart(snake[len(snake)-1]))  # create part with the end of the array as the parent
    return snake


# function to draw to screen
def draw():
    # create old board to compare new board
    oldBoard = []
    for row in range(0, height):
        oldBoard.append([])
        for item in range(0, width):
            oldBoard[row].append(v.board[row][item])  # only copy literals to avoid pythons stupid linking

    # update board and console
    message = ""  # custom banner, for use in debugging
    console = str(message)

    if not v.bordersDrawn:  # if border needs changing
        # top border
        # change position, change colour, print line
        console += "\033[2;3H" + dispCols[1] + "  " * (width+2)

        # side borders
        for y in range(3, height+4):
            console += "\033[{};3H".format(y) + "  " + "\033[{};{}H".format(y, (width*2)+5) + "  "

        # bottom border
        console += "\033[{};3H".format(height+3) + "  " * (width+2) + dispCols[3]  # and change colour back
        v.bordersDrawn = True

    # draw snake and food, update board
    for y in range(1, height+1):
        ony = []  # array of objects on line

        # get stuff on y
        for part in v.snake:  # iterate through snake
            if part.yPos == y:  # check if its on the line being drawn
                ony.append(part)

        if v.food.yPos == y:  # check if food is on line
            ony.append(v.food)

        # go across screen
        for x in range(1, width+1):
            char = dispCols[3]  # colour to write to this position
            for obj in ony:  # go though objects on line
                if obj.xPos == x:   # if its in this position
                    if type(obj) == Food:  # if it's food
                        char = dispCols[2]  # change colour
                    else:  # if it's snake
                        char = dispCols[0]

            v.board[y-1][x-1] = char  # update board with what colour is in this position
            if v.board[y-1][x-1] != oldBoard[y-1][x-1]:  # if the colour of this position has changed
                console += "\033[{};{}H{}".format(y+2, ((x+2)*2)-1, v.board[y-1][x-1] + "  ")  # log position as to be overwritten

    console += Style.RESET_ALL + "\033[{};3HScore: {}".format(height+4, v.score)  # reset the style for other outputs
    print(console)  # update screen


#################
# START RUNTIME #
#################

cls()
print(
"\n\n\n   WELCOME TO ASCII SNAKE\n\n"+
"   USE WASD OR THE ARROW KEYS TO CONTROL\n\n"+
"   THE SNAKE IS REPRESENTED WITH '{}'s\n".format(Back.GREEN+"  "+Back.RESET)+
"   THE FOOD IS REPRESENTED WITH '{}'\n".format(Back.RED+"  "+Back.RESET)+
"   THE BORDER IS REPRESENTED WITH '{}'\n\n".format(Back.WHITE+"  "+Back.RESET)+
"   PRESS 'p' OR THE SPACE BAR TO PAUSE\n\n"+
"   PRESS 'c' THEN ENTER TO CUSTOMISE COLOURS\n"+
"   OR JUST ENTER TO START PLAYING\n\n\n"+
"   (press enter to continue)"
)

start = input()
if start == "c":
    customise()
elif start == "e":
    epilepsy = 0

cls()

# spawn the stuff
v = runtimeVars()  # object for storing all variables in

lastTime = time()

while True:
    # get inputs whenever possible
    if (is_pressed("w") or is_pressed("up")) and v.snake[0].dir != "s":
        v.inp = "w"
    elif (is_pressed("a") or is_pressed("left")) and v.snake[0].dir != "d":
        v.inp = "a"
    elif (is_pressed("s") or is_pressed("down")) and v.snake[0].dir != "w":
        v.inp = "s"
    elif (is_pressed("d") or is_pressed("right")) and v.snake[0].dir != "a":
        v.inp = "d"
    elif is_pressed("p") or is_pressed("space"):
        pause()

    # update everything
    if time() - lastTime >= 1/fps:  # only update if the correct amount of time has elapsed
        for part in v.snake:
            part.up()

        # update background if epilepsy mode is enabled
        if epilepsy == 0:
            dispCols = [Back.WHITE, Back.WHITE, Back.WHITE, Back.RESET]
            epilepsy = 1
        elif epilepsy == 1:
            dispCols = [Back.RESET, Back.RESET, Back.RESET, Back.WHITE]
            epilepsy = 0

        draw()
        lastTime = time()
