"""
Charles IV
Aquarium
"""

import random, time
from cls import cls

fps = 24
depth = 22
width = 80
fish = []
sprites = ["><>", "><##>", ">#-", ">[###]>", "]<@>", ">[>-"]
backSprites = ["<><", "<##><", "-#<", "<[##]<", "<@>[", "-<]<"]


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


def getFishOnY(y):
    fOnY = []  # array with details of the fish on that y
    for f in fish:
        if f.yPos == y:  # if the fish is on that row
            fOnY.append(f)

    return fOnY


def draw():
    console = ""
    # print top of sea
    console += "-" * width + "\n"

    # lastFish = [-1]  # set the y position of the last fish printed
    for i in range(1, depth):  # iterate through the depths
        y = ""  # write to this string then write the string to console
        drawn = 0  # how many characters I have drawn on this y
        fony = getFishOnY(i)  # get the fish on that y
        #if len(fony) == 0:  # if there are no fish on that y
        if False:
            print()
        else:
            for x in range(0, width):  # go across the page
                #drawn = 0  # how many characters I have drawn on this x
                for f in fony:
                    if f.xPos == x + drawn:  # if the fish starts there
                        for char in f.sprite:  # iterate through sprite
                            if len(y) >= width:
                                break  # don't draw if it it's going off edge
                            else:
                                y += char
                                drawn += 1
                    #break  # so we don't draw two fish in the same position

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


count = 0
nextSpawn = random.randint(5, 10)

spawn()

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

    draw()

    count += 1
    if count == nextSpawn:
        spawn()
        count = 0

    time.sleep(1/fps)
