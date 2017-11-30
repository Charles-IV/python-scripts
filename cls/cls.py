
"""
Charles IV
cls - so I can use this function across files (and now it's on github across programs
"""

import os  # to clear screen if in terminal
import platform  # to detect what operating system it is being run on

win = False; lin = False; oth = False
# finding the platform being run - I run Ubuntu on my PC at home so i want some of the os.system commands to still work
if platform.system() == "Windows":
    win = True  # these booleans are for faster checking of which os is being run
elif platform.system() == "Linux":
    lin = True
    # print("It appears you are running Linux, I am porting os commands (color, cls etc) for a better experience")
else:
    oth = True
    # print("Are you running OSX? Don't care about you.")


def cls():  # to clear the terminal
    if win:
        os.system("cls")  # clearing terminal screen
    elif lin:
        os.system("reset")  # equivalent of cls for Ubuntu/Linux
    elif oth:
        os.system("reset")  # this might work for OSX
