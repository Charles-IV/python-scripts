#!/usr/bin/python3

import os, random
from time import time
from keyboard import is_pressed
from colorama import init, Fore, Back, Style

init()  # for windows

# some vars

width = 40
height = 40
fps = 10

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
                    self.up()  # try to change food postition to where the snake isn't
            for part in v.snake2:
                if part.pos == self.pos:  # if the snake is where the food just spawned
                    self.up()  # try to change food postition to where the snake isn't
        except NameError:  # if vars ahven't been inited yet
            pass  # TODO: make sure not at spawn point
        self.eaten = False  # maybe inefficient, but it makes regenerating easier
            

class SnakeHead:
    def __init__(self, player):
        self.xPos = width // 2
        if player == 1:
            self.yPos = height // 4
        elif player == 2:
            self.yPos = 3 * (height // 4)
        self.dir = "d"  # wasd - starts going right
        self.pos = str(self.xPos) + "x" + str(self.yPos)
        self.oldPos = self.pos  # so parts can follow
        self.player = player  # player 1 or 2
        self.over = False  # have a variable for this so gaveOver gan be called and the full snake array passed to it, rather than passing it needlessly through the up method.
        
        
    def up(self):#, inp):
        # get direction
        if self.player == 1:
            self.dir = v.inp  # TODO: make this more efficient, don't need duplicate variables
                        # currently I'm using this to compare the current direction to the input, so the player doesn't turn 180 and kill themselves, but it could be made more efficient
        elif self.player == 2:
            self.dir = v.inp2
        
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
            if self.player == 1:
                v.snake = spawnPart(v.snake, self.player)  # add a part to the snake
            elif self.player == 2:
                v.snake2 = spawnPart(v.snake2, self.player)
            v.food.eaten = True  # tell the food it's been eaten to respawn
            
        if (1 > self.xPos or self.xPos > width) or (1 > self.yPos or self.yPos > height):  # if off screen
            self.over = True  # tell main bit to end game and recreate vars
            
        # check if ran into other snake (can go over self)
        if self.player == 1:
            for part in v.snake2:  # iterate through the parts on the other snake
                if part.pos == self.pos:  # if other snake trapped you
                    self.over = True
        elif self.player == 2:
            for part in v.snake:  # iterate through the parts on the other snake
                if part.pos == self.pos:  # if other snake trapped you
                    self.over = True
                
                
class SnakePart:
    def __init__(self, mummy, player):
        self.parent = mummy  # mummy!
        self.pos = self.parent.oldPos  # set position to mummys old possition
        self.xPos, self.yPos = self.pos.split("x")  # set xPos and yPos
        self.xPox = int(self.xPos)
        self.yPos = int(self.yPos)
        self.oldPos = self.pos
        self.player = player  # player 1 or 2
        self.over = self.parent.over  # placeholder to make my life easier
        # TODO: most of this could probably be moved into  up() and just call up here
        
    def up(self):#, inp):  # take input but ignore it - thats mummys job
        # update old position
        self.oldPos = self.pos
        # update current possition to parents old position and update xPos and yPos
        self.pos = self.parent.oldPos
        self.xPos, self.yPos = self.pos.split("x")
        self.xPos = int(self.xPos)  # change to integers
        self.yPos = int(self.yPos)
        
        self.over = self.parent.over
        
        
class runtimeVars:  # object for storing runtime variables
    def __init__(self):
        self.reset()
        
    def reset(self):  # reset all to 0
        self.snake = []
        self.snake2 = []
        
        self.food = Food()
        
        # player 1
        self.snake.append(SnakeHead(1))
        for i in range(0, 5):  # create 5 parts
            self.snake = spawnPart(self.snake, 1)
        self.inp = "d"
        
        # player 2
        self.snake2.append(SnakeHead(2))
        for i in range(0, 5):  # create 5 parts
            self.snake2 = spawnPart(self.snake2, 2)
        self.inp2 = "d"

        self.score = 0
        """
        self.bordersDrawn = False
        
        # board to only print updates
        self.board = []
        for row in range(0, height):
            self.board.append([])
            for column in range(0, width):
                self.board[row].append(Back.RESET)  # background is probably transparent"""


#############
# FUNCTIONS #
#############

# functions called depending on what happens what happens in game
def gameOver(player):
    cls()
    print("\n\n"+
        "      _____          __  __ ______    ______      ________ _____  \n"+
        "     / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \ \n"+
        "    | |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) |\n"+
        "    | | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  / \n"+
        "    | |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \ \n"+
        "     \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_\ \n\n"+
        "   Y O U   D I E D\n\n"+
        "   Player {} lost!\n\n".format(player))
    input("   >")  # clear out all the gunk waiting to be inputed so I get y or n next
    restart = input("\033[1A   Do you want to restart? [Y/n]: ")  # ansi escape to go up one line to overwrite last line
    if restart.lower() == "n":
        exit()
    v.reset()
    # else just return
    

def pause():
    for y in range((height//4)+2, (3*(height//4))+3):  # print from a quater to three quarters down the board
    #for y in range(7, 18):  # print on lines 5-15 of board
        print("\033[{0};{2}H{1}\033[{0};{3}H{1}".format(y, Back.WHITE+"   ", width-(width//4)+4, width+(width//4)+4)+Back.RESET, end="")
        # print two white lines parallel to each other
        
    print("\033["+str(height+5)+";4HP A U S E D        (press enter to play)", end="")
    input()  # wait until enter is pressed
    print("\033[K")  # clear line with paused message on


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
    print("""
   Success!
   Colour for snake: {}\n""".format(dispCols[0]+"  "+Back.RESET)+
    "   Colour for border: {}\n".format(dispCols[1]+"  "+Back.RESET)+
    "   Colour for food: {}\n".format(dispCols[2]+"  "+Back.RESET)+
    "   Colour for background: {}\n".format(dispCols[3]+"  "+Back.RESET)+
    "\n   (continue)"
    )
    input()
   

# functions to assist with repetative functions
def cls():  # to clear screen
    print("\033[2J \033[H", end="")  # clear screen and go to 0,0, then go to 0,0 again because ansi sucks? There's a problem with Esc[2J
    # This method works when access to command prompt is blocked
    

def spawnPart(snek, player):
    snek.append(SnakePart(snek[len(snek)-1], player))  # create part with the end of the array as the parent
    return snek
        
"""
def spawnAll():
    # spawn the stuff
    snake = []
    snake2 = []
    food = Food()
    
    # player 1
    snake.append(SnakeHead(1))
    for i in range(0, 5):  # create 5 parts
        spawnPart(1)
    inp = "d"

    # player 2
    snake2.append(SnakeHead(2))
    for i in range(0, 5):  # create 5 parts
        spawnPart(2)
    inp2 = "d"
"""


# function to draw to screen
def draw():
    message = ""  # custom banner, for use in debugging
    console = str(message) + "\n"
    for y in range(0, height + 2):  # 0, height+2 for border
        ony = []
        line = "  " + dispCols[1] + "  "  # spacer and border
        # get stuff on y
        for part in v.snake:
            if part.yPos == y:
                ony.append(part)
        
        for part in v.snake2:
            if part.yPos == y:
                ony.append(part)
                
        if v.food.yPos == y:  #  if the food is on y
            ony.append(v.food)
            
        # go across screen
        for x in range(1, width + 1):
            if y == 0 or y == height + 1:  # borders
                char = dispCols[1] + "  "
            else:
                char = dispCols[3] + "  "  # character to write in that position
                for obj in ony:
                    if obj.xPos == x:  # if it's this position
                        if type(obj) == Food:  # if it's food
                            char = dispCols[2] + "  "  # overwrite character to write
                        
                        else:  # if it snake
                            if obj.player == 1:  # if snake 1
                                char = dispCols[0] + "  "
                            elif obj.player == 2:  # if snake 2
                                char = Back.BLUE + "  "  # TODO: customise player 2 colour
                        
            line += char  # write character in this position
            
        console += line + dispCols[1] + "  \n" + Back.RESET  # newline and border
        
    console += Style.RESET_ALL + "  Score: {}".format(score)  # reset the style for other outputs
    cls()  # clear screen
    print(console)  # replace it
    

#################  
# start runtime #
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

if input() == "c":
    customise()
"""
# spawn the stuff
snake = []
snake2 = []
food = Food()
# player 1
snake.append(SnakeHead(1))
for i in range(0, 5):  # create 5 parts
    spawnPart(1)
inp = "d"

# player 2
snake2.append(SnakeHead(2))
for i in range(0, 5):  # create 5 parts
    spawnPart(2)
inp2 = "d"
"""
#spawnAll()
v = runtimeVars()

score = 0
lastTime = time()
while True:
    # get inputs whenever possible
    # player 1 - wasd
    if is_pressed("w") and v.snake[0].dir != "s":
        v.inp = "w"
    elif is_pressed("a") and v.snake[0].dir != "d":
        v.inp = "a"
    elif is_pressed("s") and v.snake[0].dir != "w":
        v.inp = "s"
    elif is_pressed("d") and v.snake[0].dir != "a":
        v.inp = "d"
    # player 2 - arrow keys
    if is_pressed("up") and v.snake2[0].dir != "s":
        v.inp2 = "w"
    elif is_pressed("left") and v.snake2[0].dir != "d":
        v.inp2 = "a"
    elif is_pressed("down") and v.snake2[0].dir != "w":
        v.inp2 = "s"
    elif is_pressed("right") and v.snake2[0].dir != "a":
        v.inp2 = "d"
    # pause
    if is_pressed("p") or is_pressed("space"):
        pause()
        
    # update everything
    if time() - lastTime >= 1/fps:  # only update if the correct amount of time has elapsed
        # player 1
        for part in v.snake:
            part.up()#inp)  # parts that aren't the head will ignore inp
            if part.over:  # if game over
                """# reset the variables because gameOver can't
                snake = []
                snake.append(SnakeHead(1))
                for i in range(0, 5):  # create 5 parts
                    spawnPart(1)
                food = Food()
                inp = "d"
                gameOver(part.player)  # do the gameOver screen
                score = 0  # reset score afterwards so people can see it on the gameOver screen
                break  # break out of loop of all the parts"""
                gameOver(part.player)
                break
                
                
        # player 2
        for part in v.snake2:
            part.up()#inp2)  # parts that aren't the head will ignore inp
            if part.over:  # if game over
                """# reset the variables because gameOver can't
                snake2 = []
                snake2.append(SnakeHead(2))
                for i in range(0, 5):  # create 5 parts
                    spawnPart(2)
                food = Food()
                inp2 = "d"
                gameOver(part.player)  # do the gameOver screen
                score = 0  # reset score afterwards so people can see it on the gameOver screen
                break  # break out of loop of all the parts"""
                gameOver(part.player)
                break
            
        if v.food.eaten:  # if the food's been eaten
            v.food.up()  # respawn the food
            score += 1  # increase score
        
        
        draw()
        lastTime = time()

