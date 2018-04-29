#!/usr/bin/python3

"""
Charles IV
Aquarium
"""

import random, time#, asyncio
from shutil import get_terminal_size
from cls import cls

# set number of updates per second
fps = 17
# get size of terminal
width, depth = get_terminal_size()
prevSize = get_terminal_size()
sky = depth // 8  # sky is 1/8 of screen
depth -= sky
depth -= 1  # depth correction
# array for fish
fish = []
# arrays of sprites
sprites = ["><>", "><##>", ">#-", ">[###]>", "]<@>", ">[>-"]


def ReverseFish(revFish):
    start = [">", "<", "]", "[", "}", "{", "/", "\\"]
    code =  ["1", "2", "3", "4", "5", "6", "7", "8" ]
    end =   ["<", ">", "[", "]", "{", "}", "\\", "/"]

    for i in range(0, len(start)):
        revFish = revFish.replace(start[i], code[i])

    for i in range(0, len(end)):
        revFish = revFish.replace(code[i], end[i])

    return revFish[::-1]
    
    
class Fish:
    def __init__(self, ypos, back, sprite):
        self.yPos = ypos
        self.xPos = 0
        self.back = back
        self.speed = random.randint(1, 4)
        self.vertical = random.randint(1, 50)  # how long it takes till it goes up or down
        self.sprite = sprite
        
        if back:
            self.xPos = width
            self.speed = - self.speed
            self.sprite = ReverseFish(self.sprite)


    def up(self):
        self.xPos += self.speed
        self.vertical -= 1
        if self.vertical == 0:  # if up down counter done
            if bool(random.getrandbits(1)):  # go up or down
                self.yPos += 1
            else:
                self.yPos -= 1
            self.vertical = random.randint(1, 50)  # reset vertical counter
        
        
class ChildFish:
    def __init__(self, parent, off, sprite):
        self.parent = parent
        self.off = off
        self.sprite = sprite
        
        if parent.back:
            self.sprite = ReverseFish(self.sprite)

        # update other values
        self.up()
        
        
    def up(self):
        self.yPos = self.parent.yPos + self.off  # add offset
        self.xPos = self.parent.xPos
        self.back = self.parent.back
        self.speed = self.parent.speed


def getFishOnY(y):
    fOnY = []  # array with details of the fish on that y
    for f in fish:
        if f.yPos == y:  # if the fish is on that row
            fOnY.append(f)

    return fOnY
    

def sizeUp(width, depth, sky, prevSize):  # check terminal size
    if prevSize != get_terminal_size():  # if size has changed
        width, depth = get_terminal_size()
        prevSize = get_terminal_size()
        sky = depth // 8  # sky is 1/8 of screen
        depth -= sky
        depth -= 1  # depth correction
        
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

        for x in range(0, width):  # go across the page
            char = ""  # character to be drawn
            for f in fony:  # iterate through fish on this y
                if len(y) in range(f.xPos, f.xPos+len(f.sprite)):  # if current x is in the fish
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


# borrow this from chris coz i need at least 2
#    ________  
#\  /        \ 
# >|          >
#/  \________/ 


bigBoySprites = [[
    "   ____  ",
    "\ /   o\ ",
    " |     < ",
    "/ \____/ "],[
    "    ________  ",
    "\  /        \ ",
    " >|          >",
    "/  \________/ "]
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
    

count = 0
nextSpawn = random.randint(5, 10)
waveCount = 1

spawn()
#spawnBigBoy()


while True:
    width, depth, sky, prevSize = sizeUp(width, depth, sky, prevSize)
    for f in fish:
        f.up()
        # remove fish from array when off screen
        if not f.back:
            if f.xPos > width:
                fish.remove(f)
        else:
            if f.xPos < 0:
                fish.remove(f)
    
    draw(int(waveCount))
    
    if waveCount == 3:
        waveCount = 0.5  # it will be one at the end of the loop

    count += 1
    if count == nextSpawn:
        if bool(random.getrandbits(1)):  # spawn normal fish or big boy
            spawn()
        else:
            spawnBigBoy()
            
        count = 0
    
    waveCount += 0.5
    
    time.sleep(1/fps)
