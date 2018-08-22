import random, os, time

### NOTES:
#
# 'health' is based on the number of steps it took to get to the end
# maybe they generate a random path (step by step), record it, and that's what is mutaded
#       thus, they must die when they hit walls so it doesn't go on forever

# actually, its now going to be done on distance (x dist + y dist)
# and them i'm going going to do something with the steps (times them together?)
# and then finally get hte inverse to less distance and steps is better
# i will also square the distance to make that more impotand, and maybe only add steps

objects = []  # with all sprites in - dots, goal, etc
dots = []
goal = [10, 20]
generation = 1
populationsize = 100
stepspergen = 100

# to implement
chanceofmutation = 1/10
gridsize = [20, 20]


class Dot:
    def __init__(self, log):  # baisically everything is chosed inside init
        # Direction:
        # 1 - up, 2 - right, 3 - down, 4 - left
        #self.dir = random.randint(1, 4) - set later
        # Position:
        # 20x20 grid, start co-ordinates at (10, 1), goal at (10, 20)
        self.pos = [10, 1]
        ### Genes of the dots: (to be mutated and passed on)
        # something that makes then chose on direction more often?
        # Something that records their previous directions?
        #self.log = []  # log of all directions taken
        self.log = log
        # Fitness stuff
        self.steps = 0  # so we know how many steps are taken
        # self.fitness will be 1/self.steps - so smallest steps is biggest
        # if they're dead - so they stop moving

    def up(self):  # update function
        if self.pos != goal:  # if they havent finished
            if len(self.log) <= self.steps:  #  if there is no instruction for this move
                self.log.append(random.randint(1, 4))  # generate one
            self.dir = self.log[self.steps]
            if self.dir == 1:  # if up
                if self.pos[1] < 20:  # if they're not at the top
                    self.pos[1] += 1  # add one to y pos - 1 up
                else:
                    self.pos [1] -= 1  # go down so they don't go off screen
                    # also don't bother changing direction because I'm lazy and does it matter?
            elif self.dir == 2:  # if right
                if self.pos[0] < 20:  # if not to far right
                    self.pos[0] += 1  # add one to x pos - 1 right
                else:
                    self.pos[0] -= 1  # go left to stay on screen
            elif self.dir == 3:
                if self.pos[0] > 0:
                    self.pos[1] -= 1
                else:
                    self.pos[1] += 1
            elif self.dir == 4:
                if self.pos[0] > 0:
                    self.pos[0] -= 1
                else:
                    self.pos[0] += 1

            # update gene stuff
            #self.log.append(self.dir)
            self.steps += 1

        # nothing happens if they have reached the goal


def cls():  # function to clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')


def onLine(line):  # function to find the opbjects on that line
    o = []  # the objects on that line
    for ob in objects:  # iterate through objects
        if ob.pos[1] == line:  # if y value is same as line being printed
            o.append(ob)  # add the object to the array

    return o


def draw(gen, currstep):
    screen = ""  # what will be put onto the console
    for y in range(20, 1, -1):  # to go from 10 to 1, as 1 is at the bottom
        line = " "  # what will go onto the line - one space buffer on left
        obs = onLine(y)  # get the objects on the line
        for x in range(1, 20):  # go through the x positions on the line
            char = "-"  # character to be drawn (will be space if nothing there)

            # do goal fist so it#s overwritten by dots
            if y == goal[1] and x == goal[0]:
                char = "#"

            # go through objects on the line and add them
            for o in obs:
                if o.pos[0] == x:  # if dot is here
                    char = "o"

            line += char + " "  # add space as buffer

        screen += line + "\n"  # draw line onto screen

    screen += "\nGeneration: {}         Current Step:{}".format(gen, currstep)

    cls()  # clear the old screen
    print(screen)  # draw the new screen


def calcFit(d):  # calculate the fitness of the dot
    xdist = abs(goal[0]-d.pos[0])
    ydist = abs(goal[1]-d.pos[1])
    dist = xdist + ydist
    d.fitness = 1/((dist**2) * d.steps)


def makeBaby():  # selects a parent, mutates and returns it
    # select parent
    # get the sum of the fitnesses
    totalfitness = 0
    for d in dots:
        totalfitness += d.fitness
    # select a random number within the fitness sum
    select = random.uniform(0, totalfitness)
    # find out which dot was chosen
    currenttotal = 0
    for d in dots:
        currenttotal += d.fitness
        if currenttotal >= select:
            parent = d
            break  # exit loop so it doesn't re-register every dot after this as parent

    # mutate parents genes
    child = Dot(parent.log)
    for i in child.log:  # go through the steps in the log
        if random.randint(1, 10) == 1:  # 1/10 chance of mutation
            i = random.randint(1, 4)  # re-write direction in log

    return child


# init shit
# add goal to objects - no need - checked manually by draw() - change later
# generate dots
for x in range(0, populationsize):  # population of 10
    dots.append(Dot([]))  # generate dot with empty logs

# add them to object
for d in dots:  # go through dots
    objects.append(d)  # add the dot to the array
# idk y i didn't just add the dots straight to objects. Might be useful later?
# just leave me alove, ok?

"""
while genDone == False:  # ima gonna need to ^C this stuff
    for d in dots:
        genDone = d.up(genDone)  # do genDone stuff so we know when we're done
    draw()
    time.sleep(0.1)  # so you can see it, and to give my cpu a rest
"""

while True:  # go through infinite generations
    for i in range(1, stepspergen + 1):  # steps per generation
        for d in dots:
            d.up()
        draw(generation, i)
        time.sleep(0.1)  # so you can see it, and to give my cpu a rest
    # after each generation
    # get the fitness of the dots
    for d in dots:
        calcFit(d)

    # make new dots
    newdots = []
    for x in range(0, populationsize):
        newdots.append(makeBaby())

    # remove old dots from objects
    for d in dots:
        objects.remove(d)

    # add new dots to opbjects
    dots = newdots
    for d in dots:
        objects.append(d)

    generation += 1
