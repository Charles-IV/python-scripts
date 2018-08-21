import random, os, time

### NOTES:
#
# 'health' is based on the number of steps it took to get to the end
# maybe they generate a random path (step by step), record it, and that's what is mutaded
#       thus, they must die when they hit walls so it doesn't go on forever

objects = []  # with all sprites in - dots, goal, etc
dots = []
genDone = False


class Dot:
    def __init__(self):  # baisically everything is chosed inside init
        # Direction:
        # 1 - up, 2 - right, 3 - down, 4 - left
        #self.dir = random.randint(1, 4) - set later
        # Position:
        # 10x10 grid, start co-ordinates at (5, 1), goal at (5, 10)
        self.pos = [5, 1]
        ### Genes of the dots: (to be mutated and passed on)
        # something that makes then chose on direction more often?
        # Something that records their previous directions?
        self.log = []  # log of all directions taken
        # Fitness stuff
        self.steps = 0  # so we know how many steps are taken
        # self.fitness will be 1/self.steps - so smallest steps is biggest
        # if they're dead - so they stop moving

    def up(self):  # update function
        if self.pos == [5, 10]:  # if they're done
            genDone = True

        elif self.pos != [5, 10]:  # if they havent finished
            self.dir = random.randint(1, 4)
            if self.dir == 1:  # if up
                if self.pos[1] < 10:  # if they're not at the top
                    self.pos[1] += 1  # add one to y pos - 1 up
                else:
                    self.pos [1] -= 1  # go down so they don't go off screen
                    # also don't bother changing direction because I'm lazy and does it matter?
            elif self.dir == 2:  # if right
                if self.pos[0] < 10:  # if not to far right
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
            self.log.append(self.dir)
            self.steps += 1


def cls():  # function to clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')


def onLine(line):  # function to find the opbjects on that line
    online = []  # the objects on that line
    for ob in objects:  # iterate through objects
        if ob.pos[1] == line:  # if y value is same as line being printed
            onLine.append(ob)  # add the object to the array

    return onLine


def draw():
    screen = ""  # what will be put onto the console
    for y in range(10, 1, -1):  # to go from 10 to 1, as 1 is at the bottom
        line = ""  # what will go onto the line
        obs = onLine(y)  # get the objects on the line
        for x in range(1, 10):  # go through the x positions on the line
            char = " "  # character to be drawn (will be space if nothing there)

            # do goal fist so it#s overwritten by dots
            if y == 10 and x == 5:
                char = "#"

            # go through objects on the line and add them
            for o in obs:
                if o.pos[0] == x:  # if dot is here
                    char = "o"

            line += char + " "  # add space as buffer

        screen += line + "\n"  # draw line onto screen

    cls()  # clear the old screen
    print(screen)  # draw the new screen


# init shit
# add goal to objects - no need - checked manually by draw() - change later
# generate dots
for x in range(0, 9):  # population of 10
    dots.append(Dot)
# add them to object
for d in dots:  # go through dots
    objects.append(d)  # add the dot to the array
# idk y i didn't just add the dots straight to objects. Might be useful later?
# just leave me alove, ok?


while genDone == False:  # ima gonna need to ^C this stuff
    draw()
    time.sleep(1)  # so you can see it, and to give my cpu a rest
