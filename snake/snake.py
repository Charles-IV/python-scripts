#!/usr/bin/python3

import os, random, time
from keyboard import is_pressed
from colorama import init, Fore, Back, Style

init()  # for windows

width = 20
height = 20
fps = 10


def gameOver():
    # TODO: PROBLEM: it iterates through all the other
    #snake = []  # clear snake
    #input("died, enter")  # TODO: debugging
    cls()
    #print(snake.xPos, snake.yPos)  # TODO
    print("\n\n"+
        "      _____          __  __ ______    ______      ________ _____  \n"+
        "     / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \ \n"+
        "    | |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) |\n"+
        "    | | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  / \n"+
        "    | |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \ \n"+
        "     \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_\ \n\n"+
        "   Y O U   D I E D\n\n"+
        "   Score = {}\n\n".format(score))
    input("   >")  # clear out all the gunk waiting to be inputed so i get y or n next
    restart = input("\033[1A   Do you want to restart? [Y/n]: ")  # ansi escape to go up one line to overwrite last line
    #input(restart + str(restart == "n"))
    #restart = input()
    if restart.lower() == "n":  # TODO: maybe "\n"
        exit()
    # else just return
    """else: 
        # spawn the stuff
        #input("restarting")
        snake = []
        #print(snake)
        #input("snake arr")
        food = Food
        snake.append(SnakeHead())
        #print(snake)
        #input("snake inited with" + str(snake[0].pos))
        #return
        # TODO: other parts"""


class Food:
    def __init__(self):
        self.up()  # generate values
        
    
    def up(self):  # only run when needed
        self.xPos = random.randint(1, width)
        self.yPos = random.randint(1, height)
        self.pos = str(self.xPos) + "x" + str(self.yPos)  # makes comparing easier
        self.eaten = False  # maybe inefficient, but it makes regenerating easier
            
            
class SnakeHead:
    def __init__(self):
        self.xPos = width // 2
        self.yPos = height // 2
        self.dir = "d"  # wasd - starts going right
        self.pos = str(self.xPos) + "x" + str(self.yPos)
        self.oldPos = self.pos  # so parts can follow
        self.over = False  # have a variable for this so gaveOver gan be called and the full snake array passed to it, rather than passing it needlessly through the up method.
        
        
    def up(self, inp):
        # get direction
        self.dir = inp  # TODO: make this more efficient, don't need duplicate variables
        
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
        if self.pos == food.pos:  # if eating some food
            spawnPart()  # add a part to the snake
            #score += 1  # TODO
            food.eaten = True  # tell the food it's been eaten to respawn
            
        #if 0 > self.yPos < height+1 or 0 > self.xPos < width+1:  # if off the screen
        #    gameOver()  # m8, u ded
        if (1 > self.xPos or self.xPos > width) or (1 > self.yPos or self.yPos > height):
            #print("off screen, {}, {}".format(0 > self.xPos, self.xPos > width))  # TODO
            #gameOver()  # TODO: self for debugging
            self.over = True
            #input("ok your here" + snake[0].pos)  # TODO
            
        for part in snake[1:]:  # iterate through the parts on the snake, skipping the head
            if part.pos == self.pos:  # if you're eating yourself
                #print("eating self")  # TODO
                #gameOver()  # ouch!
                self.over = True
                
                
class SnakePart:
    def __init__(self, mummy):
        self.parent = mummy  # mummy!
        self.pos = self.parent.oldPos  # set position to mummys old possition
        self.xPos, self.yPos = self.pos.split("x")  # set xPos and yPos
        self.xPox = int(self.xPos)
        self.yPos = int(self.yPos)
        self.oldPos = self.pos
        self.over = self.parent.over  # placeholder to make my life easier
        
    def up(self, inp):  # take input but ignore it - thats mummys job
        # update old position
        self.oldPos = self.pos
        # update current possition to parents old position and update xPos and yPos
        self.pos = self.parent.oldPos
        self.xPos, self.yPos = self.pos.split("x")
        self.xPos = int(self.xPos)
        self.yPos = int(self.yPos)
        #self.xPos, self.yPos = 10,10  # TODO
        
        self.over = self.parent.over
        # TODO
        
        
def cls():  # to clear screen
    #os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[2J \033[H", end="")  # clear screen and go to 0,0, then go to 0,0 again because ansi sucks? This method works when access to command prompt is blocked
    

def spawnPart():
    snake.append(SnakePart(snake[len(snake)-1]))  # create part with the end of the array as the parent


def draw():
    message = "" #snake[0].yPos  # custom banner, for use in debugging
    console = str(message) + "\n" + Fore.GREEN + Back.GREEN + Style.BRIGHT
    for y in range(1, height + 1):
        ony = []
        line = Style.RESET_ALL + "  " + Fore.GREEN + Back.GREEN
        # get stuff on y
        for part in snake:
            if part.yPos == y:
                ony.append(part)
                
        if food.yPos == y:  #  if the food is on y
            ony.append(food)  # TODO: later, use if type(ony) == Food
            
        # go across screen
        for x in range(1, width + 1):
            line += " "  # spacer
            char = "-" #+ Style.NORMAL # character to write in that position
            for obj in ony:
                if obj.xPos == x:  # if it's this position
                    if type(obj) == Food:  # if it's food
                        char = Fore.RED + "@" + Fore.GREEN  # overwrite character to write
                    
                    else:  # if it snake
                        char = Fore.BLUE + "#" + Fore.GREEN
                        
            line += char  # write character in this position
            
        console += line + " \n"  # newline and spacer
        
    console += Style.RESET_ALL + "Score: {}".format(score)  # reset the style for other outputs
    cls()  # clear screen
    print(console)  # replace it
    
    

    
# start runtime
cls()
print(
"\n\n\n   WELCOME TO ASCII SNAKE\n\n"+
"   USE WASD TO CONTROL\n\n"+
"   THE SNAKE IS REPRESENTED WITH '#'s\n\n"+
"   THE FOOD IS REPRESENTED WITH '@'\n\n"+
"   BLANK SQUARES ARE REPRESENTED WITH '-'s\n"+
"   THERE IS A SINGLE SPACE BUFFER BETWEEN EACH SQUARE\n\n\n"+  # TODO: remove if I remove them
"   (press enter to start)")
input()

# spawn the stuff
snake = []
food = Food()
snake.append(SnakeHead())
for i in range(0, 5):  # create 5 parts
    spawnPart()
inp = "d"
score = 0
while True:
    #input("NEXT THING")  # TODO
    # get user input
    
    # update stuff
    # get inputs
    if is_pressed("w") and snake[0].dir != "s":
        inp = "w"
    elif is_pressed("a") and snake[0].dir != "d":
        inp = "a"
    elif is_pressed("s") and snake[0].dir != "w":
        inp = "s"
    elif is_pressed("d") and snake[0].dir != "a":
        inp = "d"
        
    # update everything
    for part in snake:
        part.up(inp)  # parts that aren't the head will ignore inp
        if part.over:  # if game over
            # reset the variables because gameOver can't
            snake = []
            snake.append(SnakeHead())
            for i in range(0, 5):  # create 5 parts
                spawnPart()
            food = Food()
            inp = "d"
            gameOver()  # do the gameOver screen
            score = 0
            break  # try and break out of loop of all the parts
    # input("now here" + snake[0].pos)  # TODO
        
    if food.eaten:  # if the food's been eaten
        food.up()  # update the food
        score += 1
        

    draw()
    time.sleep(1/fps)
    