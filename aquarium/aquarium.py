"""
Charles IV
Aquarium
"""

import random, time
from cls import cls

depth = 24
width = 80
fish = []
sprites = ["><>", "><##>", ">#-", ">|||||----"]


class Fish:
    def __init__(self, ypos, sprite):
        self.yPos = ypos
        self.xPos = 0
        # self.speed = speed
        self.sprite = sprite

    def up(self):
        self.xPos += 1


def draw():
    cls()
    # print top of sea
    for i in range(0, width):
        print("-", end="")

    # NOT THIS BUT ....
    """
    pos = []
    # get yPos's
    for f in fish:
        pos.append([f.yPos, f.xPos])

    
    for i in range(0, depth):
        for p in range(0, len(pos)-1):
            if i == p[0]:  # if fish is on that row
                for space in range(0, p[1])

        print()
"""
    # THIS ...
    for i in range(0, depth):  # iterate through the depths
        for f in range(0, len(fish)-1):  # iterate through the fish
            if i == fish[f].yPos:  # if there is a fish on that row
                """
                for space in range(0, fish[f].xPos):  # iterate from the left to the fish
                    print(" ")  # print a space
                # endfor
                print(fish[f].sprite)  # print the fish
                """
                print("true")
            else:  # if there isn't a fish on that row
                print()  # new row
            #endif fish is at that depth
        #endfor f in fish
    #endfor i in depths

    # END THIS STUFF


def spawn():
    y = random.randint(0, depth)
    sprite = random.randint(0, len(sprites)-1)
    fish.append(Fish(y, sprite))


count = 0
nextSpawn = random.randint(2, 10)

spawn()

while True:
    for f in fish:
        f.up()

    draw()

    #count += 1
    if count == nextSpawn:
        spawn()
        count = 0

    time.sleep(1)
