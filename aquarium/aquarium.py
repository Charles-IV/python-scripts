"""
Charles IV
Aquarium
"""

import random, time
from cls import cls

depth = 24
width = 80
fish = []
sprites = ["><>", "><##>", ">#-", ">[###]>", "]<@>", ">[>-"]


class Fish:
    def __init__(self, ypos, sprite):
        self.yPos = ypos
        self.xPos = 0
        # self.speed = speed
        self.sprite = sprite

    def up(self):
        self.xPos += 1


def getFishOnY(y):
    fOnY = []  # array with details of the fish on that y
    for f in fish:
        if f.yPos == y:  # if the fish is on that row
            fOnY.append(f)

    return fOnY


def draw():
    cls()
    # print top of sea
    for i in range(0, width):
        print("-", end="")

    # lastFish = [-1]  # set the y position of the last fish printed
    for i in range(1, depth):  # iterate through the depths
        fony = getFishOnY(i)  # get the fish on that y
        if len(fony) == 0:  # if there are no fish on that y
            print()
        else:
            for x in range(0, width):  # go across the page
                drawn = 0  # how many characters I have drawn on this x
                for f in fony:
                    if f.xPos == x + drawn:  # if the fish starts there
                        print(f.sprite, end="")
                        drawn += len(f.sprite)

                if drawn == 0:  # if still haven't drawn sprite
                    print(" ", end="")  # draw space and go to next x
                    
        print()          


def spawn():
    y = random.randint(1, depth)
    sprite = random.randint(0, len(sprites)-1)
    fish.append(Fish(y, sprites[sprite]))


count = 0
nextSpawn = random.randint(5, 20)

spawn()

while True:
    for f in fish:
        f.up()

    draw()

    count += 1
    if count == nextSpawn:
        spawn()
        count = 0

    time.sleep(0.5)
