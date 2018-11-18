#!/usr/bin/python3

import os, random, time
from keyboard import is_pressed
from colorama import init, Fore, Back, Style

init()  # for windows

width = 20
height = 20
fps = 10


def gameOver():
    cls()
    print("\n\n"+
        "      _____          __  __ ______    ______      ________ _____  \n"+
        "     / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \ \n"+
        "    | |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) |\n"+
        "    | | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  / \n"+
        "    | |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \ \n"+
        "     \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_\ \n\n"+
        "   Y O U   D I E D\n\n"+
        "   Score = {}\n\n".format(score))
    input("   >")  # clear out all the gunk waiting to be inputed so I get y or n next
    restart = input("\033[1A   Do you want to restart? [Y/n]: ")  # ansi escape to go up one line to overwrite last line
    if restart.lower() == "n":
        exit()
    # else just return


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
        if self.pos == food.pos:  # if eating some food
            spawnPart()  # add a part to the snake
            food.eaten = True  # tell the food it's been eaten to respawn
            
        if (1 > self.xPos or self.xPos > width) or (1 > self.yPos or self.yPos > height):  # if off screen
            self.over = True  # tell main bit to end game and recreate vars
            
        for part in snake[1:]:  # iterate through the parts on the snake, skipping the head
            if part.pos == self.pos:  # if you're eating yourself
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
        # TODO: most of this could probably be moved into  up() and just call up here
        
    def up(self, inp):  # take input but ignore it - thats mummys job
        # update old position
        self.oldPos = self.pos
        # update current possition to parents old position and update xPos and yPos
        self.pos = self.parent.oldPos
        self.xPos, self.yPos = self.pos.split("x")
        self.xPos = int(self.xPos)  # change to integers
        self.yPos = int(self.yPos)
        
        self.over = self.parent.over
        
        
def cls():  # to clear screen
    print("\033[2J \033[H", end="")  # clear screen and go to 0,0, then go to 0,0 again because ansi sucks? There's a problem with Esc[2J
    # This method works when access to command prompt is blocked
    

def spawnPart():
    snake.append(SnakePart(snake[len(snake)-1]))  # create part with the end of the array as the parent


def draw():
    message = ""  # custom banner, for use in debugging
    console = str(message) + "\n"
    for y in range(0, height + 2):  # 0, height+2 for border
        ony = []
        line = "  " + Back.WHITE + "  " + Style.RESET_ALL  # spacer and border
        # get stuff on y
        for part in snake:
            if part.yPos == y:
                ony.append(part)
                
        if food.yPos == y:  #  if the food is on y
            ony.append(food)  # TODO: later, use if type(ony) == Food
            
        # go across screen
        for x in range(1, width + 1):
            if y == 0 or y == height + 1:  # borders
                char = Back.WHITE + "  "
            else:
                char = "  "  # character to write in that position
                for obj in ony:
                    if obj.xPos == x:  # if it's this position
                        if type(obj) == Food:  # if it's food
                            char = Back.RED + "  " + Style.RESET_ALL  # overwrite character to write
                        
                        else:  # if it snake
                            char = Fore.GREEN + Back.GREEN + "  " + Style.RESET_ALL
                        
            line += char  # write character in this position
            
        console += line + Back.WHITE + "  \n" + Style.RESET_ALL  # newline and border
        
    console += Style.RESET_ALL + "  Score: {}".format(score)  # reset the style for other outputs
    cls()  # clear screen
    print(console)  # replace it
    

#################  
# start runtime #
#################

cls()
print(
"\n\n\n   WELCOME TO ASCII SNAKE\n\n"+
"   USE WASD TO CONTROL\n\n"+
"   THE SNAKE IS REPRESENTED WITH '{}'s\n".format(Back.GREEN+"  "+Style.RESET_ALL)+
"   THE FOOD IS REPRESENTED WITH '{}'\n".format(Back.RED+"  "+Style.RESET_ALL)+
"   THE BORDER IS REPRESENTED WITH '{}'\n\n\n".format(Back.WHITE+"  "+Style.RESET_ALL)+
"   (press enter to start)"
)
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
            score = 0  # reset score afterwards so people can see it on the gameOver screen
            break  # break out of loop of all the parts
        
    if food.eaten:  # if the food's been eaten
        food.up()  # respawn the food
        score += 1  # increase score
        

    draw()  # draw the current screen
    time.sleep(1/fps)  # slow down so it's playable

