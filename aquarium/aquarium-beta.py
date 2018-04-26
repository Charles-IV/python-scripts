"""
Charles IV
Aquarium
"""

import random, time, asyncio
from shutil import get_terminal_size
from cls import cls

# set number of updates per second
fps = 15
# get size of terminal
width, depth = get_terminal_size()
sky = depth // 8  # sky is 1/8 of screen
depth -= sky
depth -= 2  # depth correction
# array for fish
fish = []
# arrays of sprites
sprites = ["><>", "><##>", ">#-", ">[###]>", "]<@>", ">[>-"]
backSprites = ["<><", "<##><", "-#<", "<[###]<", "<@>[", "-<]<"]


class Fish:
    def __init__(self, ypos, back, sprite):
        if not back:  # if left -> right
            self.yPos = ypos
            self.xPos = 0
            self.back = back
            self.speed = random.randint(1, 4)
            self.sprite = sprite
        else:  # if right -> left
            self.yPos = ypos
            self.xPos = width
            self.back = back
            self.speed = - random.randint(1, 4)
            self.sprite = sprite


    def up(self):
        self.xPos += self.speed
        
        
class ChildFish:
    def __init__(self, parent, off, sprite):
        self.parent = parent
        self.off = off
        self.sprite = sprite
        
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
    

async def sizeUp():  # check terminal size
    global width, depth, sky
    while True:
        await asyncio.sleep(1/fps)
        if (width, (depth+sky+2)) != get_terminal_size():  # if size has changed
            width, depth = get_terminal_size()
            sky = depth // 8  # sky is 1/8 of screen
            depth -= sky
            depth -= 2  # depth correction
            

def draw(wave):
    # print sky
    console = "\n" * sky + "\n"
    #console = ""
    
    # print top of sea
    if wave == 1:
        console += "_--" * (width//3) + "\n"
    
    elif wave == 2:
        console += "-_-" * (width//3) + "\n"
        
    elif wave == 3:
        console += "--_" * (width//3) + "\n"

    for i in range(1, depth):  # iterate through the depths
        y = ""  # write to this string then write the string to console
        drawn = 0  # how many characters I have drawn on this y
        fony = getFishOnY(i)  # get the fish on that y
        if len(fony) == 0:  # if there are no fish on that y
            print()
        else:
            for x in range(0, width):  # go across the page
                #drawn = 0  # how many characters I have drawn on this x
                for f in fony:
                    if f.xPos == (x + drawn):  # if the fish starts there
                        for char in f.sprite:  # iterate through sprite
                            if len(y) >= width:
                                break  # don't draw if it it's going off edge
                            else:
                                y += char
                                drawn += 1
                    break  # so we don't draw two fish in the same position
                    # this actually just doesn't print the fish if it is on the same line but oh well

                if drawn == 0:  # if still haven't drawn sprite
                    if x + drawn <= width:
                        y += " "
                    
        console += y + "\n"
        
    cls()
    print(console)


def spawn():
    y = random.randint(2, depth)
    backwards = bool(random.getrandbits(1))  # if fish is going from left to right or right to 
    if backwards:  # if right -> left
        fish.append(Fish(y, backwards, sprite = random.choice(backSprites)))  # use backwards sprite
    else:
        fish.append(Fish(y, backwards, sprite = random.choice(sprites)))


# big boys

# sprites:

#   ____  
#\ /   o\ 
# |     < 
#/ \____/
# ___    
#/o  \ / 
#>    |  
#\___/ \ 

# borrow this from chris coz i need at least 2
#    ________  
#\  /        \ 
# >|          >
#/  \________/ 
#  ________     
# /        \  / 
#<          |<  
# \________/  \ 

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

backBigBoySprites = [[
    " ___    ",
    "/o  \ / ",
    ">    |  ",
    "\___/ \ "],[
    "  ________     ",
    " /        \  / ",
    "<          |<  ",
    " \________/  \ "]
]


def spawnBigBoy():
    # generate parent
    backwards = bool(random.getrandbits(1))  # if fish is going from left to right or right to 
    sprite = random.randint(1, len(bigBoySprites)-1)
    y = random.randint(2, depth - len(bigBoySprites))
    if backwards:  # if right -> left
        par = Fish(y, backwards, sprite = backBigBoySprites[sprite][0])  # use backwards sprite
    else:
        par = Fish(y, backwards, sprite = bigBoySprites[sprite][0])
        
    fish.append(par)  # add parent to fish
    
    
    # generate children
    if backwards:
        #for s in backBigBoySprites[sprite]:  # iterate through sprite
        for s in range(1, len(backBigBoySprites[sprite])):  # iterate through positions in sprite
            fish.append(ChildFish(par, s, backBigBoySprites[sprite][s]))  # add child to fish
            
    else:
        for s in range(1, len(bigBoySprites[sprite])):  # iterate through positions in sprite
            fish.append(ChildFish(par, s, bigBoySprites[sprite][s]))  # add child to fish
    

count = 0
nextSpawn = random.randint(5, 10)
waveCount = 1

spawn()
spawnBigBoy()


async def main():
    global count, nextSpawn, waveCount
    while True:        
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
        
        await asyncio.sleep(1/fps)


loop = asyncio.get_event_loop()
asyncio.ensure_future(main())
asyncio.ensure_future(sizeUp())
loop.run_forever()
