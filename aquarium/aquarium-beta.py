#!/usr/bin/python3

"""
Charles IV
Aquarium
"""

import random, time
from shutil import get_terminal_size
from cls import cls
from keyboard import is_pressed

# set number of updates per second
fps = 18
# get size of terminal
width, depth = get_terminal_size()
prevSize = get_terminal_size()
sky = depth // 8  # sky is 1/8 of screen
depth -= sky
depth -= 3  # depth correction
# arrays for objects
fish = []
bubbles = []
# array of sprites
sprites = ["><>", "><##>", ">#-", ">[###]>", "]<@>", ">[>-", "><(((('>"]



def ReverseFish(revFish):
    start = [">", "<", "]", "[", "}", "{", "/", "\\", "(", ")"]
    code  = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "a" ]
    end   = ["<", ">", "[", "]", "{", "}", "\\", "/", ")", "("]

    for i in range(0, len(start)):
        revFish = revFish.replace(start[i], code[i])

    for i in range(0, len(end)):
        revFish = revFish.replace(code[i], end[i])

    return revFish[::-1]
    
    
class Fish:
    def __init__(self, ypos, back, sprite):
        self.yPos = ypos
        self.xPos = - len(sprite)  # so it slowly comes onto the screen
        self.back = back
        self.speed = random.randint(1, 4)
        self.vertical = random.randint(1, 50)  # how long it takes till it goes up or down
        self.sprite = sprite
        
        if back:
            self.xPos = width
            self.speed = - self.speed
            self.sprite = ReverseFish(self.sprite)
            
        # turning stuff
        self.nextTurn = random.randint(2, 50)
        self.turning = False
        self.oldLen = len(sprite)
        self.halfTurned = False
        self.oldSprite = self.sprite  # so we know what it is when turning


    def up(self):
        if not self.turning:
            self.nextTurn -= 1
            if self.nextTurn == 0:  # if now need to turn
                self.turning = True
                self.nextTurn = random.randint(2, 50)  # reset turn count
                
            self.xPos += self.speed
            self.vertical -= 1
            if self.vertical == 0:  # if up down counter done
                if bool(random.getrandbits(1)):  # go up or down
                    self.yPos += 1
                else:
                    if self.yPos > 1:  # if not at top
                        self.yPos -= 1  # let it go up
                self.vertical = random.randint(1, 50)  # reset vertical counter
                
        else:  # if turning
            if not self.back:
                if not self.halfTurned:  # if still going forward
                    self.xPos += 1
                    self.sprite = self.sprite[:-1]  # remove last character
                    if len(self.sprite) == 0:  # if run out of characters
                        self.halfTurned = True
                        self.speed = - self.speed
                        self.sprite = ReverseFish(self.oldSprite)[0]  # put first character in place
                        
                else:  # if now going backwards
                    self.xPos -= 1
                    self.sprite += ReverseFish(self.oldSprite)[len(self.sprite)]  # add next character
                    if len(self.sprite) == self.oldLen:  # if done
                        self.turning = False  # finally!
                        self.halfTurned = False
                        self.back = True
                        self.oldSprite = self.sprite
                        
            else:
                if not self.halfTurned:  # if still going backwards
                    self.sprite = self.sprite[1:]  # remove first character
                    if len(self.sprite) == 0:  # if run out of characters
                        self.halfTurned = True
                        self.speed = - self.speed
                        self.sprite = ReverseFish(self.oldSprite)[-1]  # put first character in place
                        
                else:  # if now going forwards
                    self.sprite = ReverseFish(self.oldSprite)[-(len(self.sprite)+1)] + self.sprite # add next character
                    if len(self.sprite) == self.oldLen:  # if done
                        self.turning = False  # finally!
                        self.halfTurned = False
                        self.back = False
                        self.oldSprite = self.sprite
        
        
class ChildFish:
    def __init__(self, parent, off, sprite):
        self.parent = parent
        self.off = off
        self.sprite = sprite
        
        if parent.back:
            self.sprite = ReverseFish(self.sprite)
            
        # turning stuff
        self.oldLen = len(self.sprite)
        self.oldSprite = self.sprite  # so we know what it is when turning
        
        # update other values
        self.up()
        
        
    def up(self):
        self.yPos = self.parent.yPos + self.off  # add offset
        self.xPos = self.parent.xPos
        self.back = self.parent.back
        # self.speed = self.parent.speed - do we even need this
        
        # turning stuff
        # self.nextTurn = self.parent.nextTurn
        # self.turning = self.parent.turning - done by parent (dbp)  TODO: remove when done
        #self.oldLen = len(self.sprite) - don't want to update every time
        # self.halfTurned = self.parent.halfTurned
        #self.oldSprite = self.sprite  # so we know what it is when turning
        
        if self.parent.turning:
            if not self.parent.back:
                if not self.parent.halfTurned:  # if still going forward
                    # self.xPos += 1 - dbp
                    self.sprite = self.sprite[:-1]  # remove last character
                    if len(self.sprite) == 0:  # if run out of characters
                        # self.halfTurned = True
                        # self.speed = - self.speed - don't need speed
                        self.sprite = ReverseFish(self.oldSprite)[0]  # put first character in place
                        
                else:  # if now going backwards
                    # self.xPos -= 1 -dbp
                    self.sprite += ReverseFish(self.oldSprite)[len(self.sprite)]  # add next character
                    if len(self.sprite) == self.oldLen:  # if done
                        # self.turning = False  # finally!
                        # self.halfTurned = False
                        # self.back = True - dbp
                        self.oldSprite = self.sprite
                        
            else:
                if not self.parent.halfTurned:  # if still going backwards
                    self.sprite = self.sprite[1:]  # remove first character
                    if len(self.sprite) == 0:  # if run out of characters
                        # self.halfTurned = True - dbp
                        # self.speed = - self.speed - don't need speed
                        self.sprite = ReverseFish(self.oldSprite)[-1]  # put first character in place
                        
                else:  # if now going forwards
                    self.sprite = ReverseFish(self.oldSprite)[-len(self.sprite)-1] + self.sprite # add next character
                    if len(self.sprite) == self.oldLen:  # if done
                        # self.turning = False  # finally!
                        # self.halfTurned = False
                        # self.back = False - dbp
                        self.oldSprite = self.sprite


class Bubble:
    def __init__(self, ypos, xpos):
        self.yPos = ypos
        self.xPos = xpos
        self.speed = random.randint(1, 2)
        self.horizontal = random.randint(1, 3)
        self.sprite = "o"
        
    
    def up(self):
        self.yPos -= self.speed
        self.horizontal -= 1
        if self.horizontal == 0:
            if bool(random.getrandbits(1)):  # go right or left
                self.xPos += 1
            else:
                self.xPos -= 1
            self.horizontal = random.randint(1, 3)  # reset horizontal counter
            
            
class PlayerFish:
    def __init__(self):
        self.sprite = "__£££££____|\____££"  # top of shark
        self.yPos = random.randint(2, depth)
        self.xPos = 0
        self.back = False
        self.speed = 0
        
        # turning stuff
        self.turning = False
        self.oldLen = len(self.sprite)
        self.halfTurned = False
        self.oldSprite = self.sprite  # so we know what it is when turning


    def up(self, inp):
        if not self.turning:
            # check position
            if self.xPos < 0 - (len(self.sprite) // 2):  # if halfway off screen
                self.speed = 5  # bounce over to the right
                
            elif self.xPos > width - (len(self.sprite) // 2):
                self.speed = -5
                
            # check their input
            if inp == "w":
                if self.yPos > 1:  # if it's not at the top, let it go up
                    self.yPos -= 1
            elif inp == "s":
                if self.yPos < depth:  # if it's not at the bottom, let it go down
                    self.yPos += 1

            elif inp == "a":
                self.speed -= 1
                if not self.back:
                    if self.speed < 1:  # if about to turn
                        self.turning = True

            elif inp == "d":
                self.speed += 1
                if self.back:
                    if self.speed > -1:  # if about to turn
                        self.turning = True
                
            # momentum type thing
            self.speed *= 0.9
                
            self.xPos += int(self.speed)
            
        else:  # if turning
            if not self.back:
                if not self.halfTurned:  # if still going forward
                    self.xPos += 1
                    self.sprite = self.sprite[:-1]  # remove last character
                    if len(self.sprite) == 0:  # if run out of characters
                        self.halfTurned = True
                        #self.speed = - self.speed
                        self.sprite = ReverseFish(self.oldSprite)[0]  # put first character in place
                        
                else:  # if now going backwards
                    self.xPos -= 1
                    self.sprite += ReverseFish(self.oldSprite)[len(self.sprite)]  # add next character
                    if len(self.sprite) == self.oldLen:  # if done
                        self.turning = False  # finally!
                        self.halfTurned = False
                        self.back = True
                        self.oldSprite = self.sprite
                        
            else:
                if not self.halfTurned:  # if still going backwards
                    self.sprite = self.sprite[1:]  # remove first character
                    if len(self.sprite) == 0:  # if run out of characters
                        self.halfTurned = True
                        #self.speed = - self.speed
                        self.sprite = ReverseFish(self.oldSprite)[-1]  # put first character in place
                        
                else:  # if now going forwards
                    self.sprite = ReverseFish(self.oldSprite)[-(len(self.sprite)+1)] + self.sprite # add next character
                    if len(self.sprite) == self.oldLen:  # if done
                        self.turning = False  # finally!
                        self.halfTurned = False
                        self.back = False
                        self.oldSprite = self.sprite
            
        

def getFishOnY(y):
    fOnY = []  # array with details of the fish on that y
    for f in fish:
        if f.yPos == y:  # if the fish is on that row
            fOnY.append(f)
            
    if playable == "1":  # if playable mode
        if player.yPos == y:  # if player is on that y
            fOnY.append(player)  # add player to array of fish
            
        for f in fOnY:
            if type(f) == ChildFish:  # if child
                if f.parent == player:  # if part of player
                    fOnY.remove(f)
                    fOnY.append(f)  # move spite to back, so it's on top

    return fOnY
    
    
def getBubOnY(y):
    bubOnY = []  # array with bubbles on y
    for b in bubbles:
        if b.yPos == y:  # if bubble on row
            bubOnY.append(b)
            
    return bubOnY
    

def sizeUp(width, depth, sky, prevSize):  # check terminal size
    if prevSize != get_terminal_size():  # if size has changed
        width, depth = get_terminal_size()
        prevSize = get_terminal_size()
        sky = depth // 8  # sky is 1/8 of screen
        depth -= sky
        depth -= 3  # depth correction
        
    return width, depth, sky, prevSize
            

def draw(wave):
    # print sky
    console = "\n" * sky + "\n"
    
    # print top of sea
    if wave == 1:
        console += "_--" * (width//3) + "\n"
    
    elif wave == 2:
        console += "-_-" * (width//3) + "\n"
        
    elif wave == 3:
        console += "--_" * (width//3) + "\n"

    for i in range(1, depth):  # iterate through the depths
        y = ""  # write to this string then write the string to console
        fony = getFishOnY(i)  # get the fish on that y
        bubony = getBubOnY(i)  # get bubbles on that y

        for x in range(0, width):  # go across the page
            char = ""  # character to be drawn
            
            # go through bubbles first so they are overwritten by fish
            for b in bubony:
                if len(y) == b.xPos:
                    char = b.sprite
                    
            for f in fony:  # iterate through fish on this y
                if len(y) in range(f.xPos, f.xPos+len(f.sprite)):  # if current x is in the fish
                    if f.sprite[len(y) - f.xPos] != "£":
                        char = f.sprite[len(y) - f.xPos]  # change the char that's being written

            if char == "":
                if len(y) <= width:
                    char = " "
            
            y += char  # draw character to y
                    
        console += y + "\n"  # draw y to screen
        
    cls()  # clear old screen
    print(console)  # draw new screen


def spawn():
    y = random.randint(2, depth)
    backwards = bool(random.getrandbits(1))  # if fish is going from left to right or right to left
    fish.append(Fish(y, backwards, sprite = random.choice(sprites)))


# big boys

# sprites:

#   ____  
#\ /   o\ 
# |     < 
#/ \____/
#    ________  
#\  /        \ 
# >|          >
#/  \________/ 
#__     ____|\____  
#\ \___/        0 \ 
# | ___           < 
#/_/   \___\_\____/ 
#                               |\               
#                               | \              
#___                _____|\_____|  \_________    
#\  \              /                         \   
# \  \            /                       @   \  
#  \  \_|\_______/                           _ \ 
#   \                <             \ \      / \/ 
#    |               <              \ \    |     
#   /  _  _______                    \ \   \/\__ 
#  /  / |/       \                             / 
# /  /            \                           /  
#/__/              \______  ___/_/_/_/__  ___/   
#                         |/            |/       
#  ____|\__        
#>[________)==>----
#|\   \\\\__  
#| \_/    o \ 
#> _   (( <_  
#| / \__+___/ 
#|/     |/
#     |\    
#    |  \   
#|\ /    .\ 
#| |       (
#|/ \     / 
#    |  /   
#     |/
#      \/)/)    
#    _'  oo(_.-.
#  /'.     .---'
#/'-./    (     
#)     ; __\    
#\_.'\ : __|    
#     )  _/     
#    (  (,.     
#     '-.-'     


bigBoySprites = [[
    "£££____££",
    "\£/   o\£",
    " |     <£",
    "/£\____/£"],[
    "£££££|\££££",
    "££££|  \£££",
    "|\£/    .\£",
    "| |       (",
    "|/£\     /£",
    "££££|  /£££",
    "£££££|/££££"],[
    "|\£££\\\\\\\\__££",
    "| \_/    o \£",
    "> _   (( <_££",
    "| /£\__+___/£",
    "|/£££££|/££££"],[
    "££££________££",
    "\££/        \£",
    " >|          >",
    "/££\________/£"],[
    "££££££\/)/)££££",
    "££££_'  oo(_.-.",
    "££/'.     .---'",
    "/'-./    (£££££",
    ")     ; __\££££",
    "\_.'\ : __|££££",
    "£££££)  _/£££££",
    "££££(  (,.£££££",
    "£££££'-.-'£££££"],[
    "££____|\__££££££££",
    ">[________)==>----"],[
    "__£££££____|\____££",
    "\ \___/        0 \£",
    " | ___           <£",
    "/_/£££\___\_\____/£"],[
    "£££££££££££££££££££££££££££££££|\£££££££££££££££",
    "£££££££££££££££££££££££££££££££| \££££££££££££££",
    "___££££££££££££££££_____|\_____|  \_________££££",
    "\  \££££££££££££££/                         \£££",
    " \  \££££££££££££/                       @   \££",
    "  \  \_|\_______/                           _ \£",
    "   \                <             \ \      /£\/£",
    "    |               <              \ \    |£££££",
    "   /  _  _______                    \ \   \/\__£",
    "  /  /£|/£££££££\                             /£",
    " /  /££££££££££££\                           /££",
    "/__/££££££££££££££\______  ___/_/_/_/__  ___/£££",
    "£££££££££££££££££££££££££|/££££££££££££|/£££££££"]
    
]


def spawnBigBoy():
    # generate parent
    backwards = bool(random.getrandbits(1))  # if fish is going from left to right or right to 
    sprite = random.randint(0, len(bigBoySprites)-1)
    y = random.randint(2, depth - len(bigBoySprites) - 2)
    par = Fish(y, backwards, sprite = bigBoySprites[sprite][0])
        
    fish.append(par)  # add parent to fish
    
    
    for s in range(1, len(bigBoySprites[sprite])):  # iterate through positions in sprite
        fish.append(ChildFish(par, s, bigBoySprites[sprite][s]))  # add child to fish
    

def spawnBubble():
    y = random.randint(2, depth)
    x = random.randint(0, width)
    bubbles.append(Bubble(y, x))  # add bubble to array


def spawnPlayer():
    player = PlayerFish()
    spriteIndex = bigBoySprites.index([
        "__£££££____|\____££",
        "\ \___/        0 \£",
        " | ___           <£",
        "/_/£££\___\_\____/£"])  # find index of sprite
    
    for i in range(1, len(bigBoySprites[spriteIndex])):  # iterate through other positions in sprite
        fish.append(ChildFish(player, i, bigBoySprites[spriteIndex][i]))  # add child to fish
        
    return player
    

# Start

cls()
print("\n\n\n\n",
"       Welcome to Aquarium!  (def not a copy of fish)\n\n",
"       Do you want to:\n",
"           1. Use playable fish (WASD)\n",
"           2. Normal mode")
#playGood = False  # if their input is good or bad
while True:
    playable = input("\n        >>>")
    if playable != "1" and playable != "2":
        print("\n        Error:\n             Please enter '1' or '2' without speech marks")
    else:  # if good input
        break  # exit loop
        
cls()
print("\n\n\n\n",
"       On Windows, make sure the console buffer is larger than the actual\n        size\n\n",
"       F11 should also improve performance\n\n\n",
"       Adjust the fps variable near the top of aquarium.py if experiencing\n        flickering.\n\n",
"       On slower systems, you may be able to comment the\n        `time.sleep(1/fps)` line at the bottom\n",
"       (put a # at the start of that line if you're a python n00b)")
input("\n     (Press enter to continue)")

nextSpawn = random.randint(5, 20)
nextBubble = random.randint(5, 10)
waveCount = 1

# spawn one of everything at start
spawn()
spawnBigBoy()
spawnBubble()
if playable == "1":  # if playable mode
    player = spawnPlayer()  # spawn player fish


while True:
    width, depth, sky, prevSize = sizeUp(width, depth, sky, prevSize)
    
    if playable == "1":  # if player mode
        # get player input
        if is_pressed("w"):  # there must be a more efficient way of doing this
            player.up("w")
        elif is_pressed("a"):
            player.up("a")
        elif is_pressed("s"):
            player.up("s")
        elif is_pressed("d"):
            player.up("d")
        else:
            player.up("null")  # still update sprite - to run checks on position etc.
        
    
    for f in fish:
        f.up()
        # remove fish from array when off screen
        if not f.back:
            if f.xPos > width:
                fish.remove(f)
        else:
            if f.xPos < 0 - len(f.sprite):
                fish.remove(f)
    
    for b in bubbles:
        b.up()
        if b.yPos == 0:
            bubbles.remove(b)
    
    draw(int(waveCount))
    
    if waveCount == 3:
        waveCount = 0.5  # it will be one at the end of the loop


    nextSpawn -= 1
    if nextSpawn == 0:
        if bool(random.getrandbits(1)):  # spawn normal fish or big boy
            spawn()
        else:
            spawnBigBoy()
        
        nextSpawn = random.randint(5, 20)
        
    nextBubble -= 1
    if nextBubble == 0:
        spawnBubble()
        
        nextBubble = random.randint(5, 10)
    
    waveCount += 0.5
    
    time.sleep(1/fps)
    
