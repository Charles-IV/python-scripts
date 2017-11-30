"""
Charles IV
RPG Fighter
"""
# Upon looking back at this, I realise this is very inefficient.
# I had just learnt how to use functions so I used them.
# - But only for modularity, not efficiency.

import random; import os; import time


def create(x):  # x is char name. x is for speed if it
    if os.path.exists(x + ".txt"):  # checks if the file already exists
        print("The character already exists. Enter a different name next time.")
        main()
    else:
        f = open(x + ".txt", "w")  # creates the file
        f.close()  # closes the file
        # print("Generating strength variable\n...")
        # st = random.randint(1, 6)  # generates a number for the strength variable
        # print("The value is", st, "do you want to continue?")
        # stChoice = input("y or n")
        
        # The following bit is (very) inefficient. You should use another function and just pass a few variables through
        
        stChoice = "y"  # If they want to re-roll. Set to yes so it does the first roll
        rerollNumber = 1  # so they don't get infinite re-rolls
        while stChoice == "y":
        
            if rerollNumber >= 5:
                print("out of rerolls")
                stChoice = "n"  # so it doesn't roll again

            else:
                print("Generating strength variable\n...")
                st = random.randint(1, 6)
                print("The value is", st, "do you want to reroll?")
                stChoice = input("y or n")
                rerollNumber += 1


        f = open(x + ".txt", "a")  # opens the file as append
        f.write(str(st)+"\n")  # appends strength variable to the file

        agiChoice = "y"
        rerollNumber = 1
        while agiChoice == "y":

            if rerollNumber >= 5:
                print("out of rerolls")
                agiChoice = "n"

            else:
                print("Generating agility variable\n...")
                agi = random.randint(1, 6)
                print("The value is", agi, "do you want to reroll?")
                agiChoice = input("y or n")
                rerollNumber += 1

        f.write(str(agi)+"\n")  # appends agility variable to the file

        print("Generating dexterity variable\n...")
        dexChoice = "y"
        rerollNumber = 1
        while dexChoice == "y":

            if rerollNumber >= 5:
                print("out of rerolls")
                dexChoice = "n"

            else:
                print("Generating dexterity variable\n...")
                dex = random.randint(1, 6)
                print("The value is", dex, "do you want to reroll?")
                dexChoice = input("y or n")
                rerollNumber += 1

        f.write(str(dex)+"\n")

        print("Generating intelligence variable\n...")

        intChoice = "y"
        rerollNumber = 1
        while intChoice == "y":

            if rerollNumber >= 5:
                print("out of rerolls")
                intChoice = "n"

            else:
                print("Generating intelligence variable\n...")
                int = random.randint(1, 6)
                print("The value is", int, "do you want to reroll?")
                intChoice = input("y or n")
                rerollNumber += 1

        f.write(str(int)+"\n")

        print("Generating luck variable\n...")

        lukChoice = "y"
        rerollNumber = 1
        while lukChoice == "y":
            if rerollNumber >= 5:
                print("out of rerolls")
                lukChoice = "n"

            else:
                print("Generating luck variable\n...")
                luk = random.randint(1, 6)
                print("The value is", dex, "do you want to reroll?")
                lukChoice = input("y or n")
                rerollNumber += 1

        f.write(str(luk)+"\n")

        f.close()  # close file to avoid errors
        print("Done!")
        main()  # goes back to the main menu


def view(x):  # x is for the character name
    if os.path.exists(x+".txt"):  # check it character file exists
        f = open(x+".txt", "r")
        print("The stats for", x, "are:\n"
              "Strength:", str(f.readline()), "\n"
              "Agility:", str(f.readline()), "\n"
              "Dexterity:", str(f.readline()), "\n"
              "Intelligence:", str(f.readline()), "\n"
              "Luck:", str(f.readline()), "\n"
        )
        f.close()
        main()

    else:
        print("This character does not exist.")
        main()


def fight(x, y):  # x is for character 1, y is for character 2
    if os.path.exists(x+".txt") and os.path.exists(y+".txt"):  # If both caracters exist
        f1 = open(x + ".txt", "r")  # open them
        f2 = open(y + ".txt", "r")
        """ dont need this any more, using 2d array
        f1st = f1.readline()
        f1agi = f1.readline()
        f1dex = f1.readline()
        f1int = f1.readline()
        f1luk = f1.readline()

        f2st = f2.readline()
        f2agi = f2.readline()
        f2dex = f2.readline()
        f2int = f2.readline()
        f2luk = f2.readline()
        """

        print("Calculating which tests to use\n...")
        test1 = random.randint(0, 4)
        test2 = random.randint(0, 4)
        test3 = random.randint(0, 4)

        while test1 == test2 or test1 == test3 or test2 == test3:
            test1 = random.randint(0, 4)  # this continues looping until they have different values
            test2 = random.randint(0, 4)
            test3 = random.randint(0, 4)

        # the following variable is nicked from Chris, because it's really clever and the only efficient way of doing it
        # I will reference it with statNames[the_number_of_the_stat]
        statNames = ["Strength", "Agility", "Dexterity", "Intelligence", "Luck"]

        # changing it into a 2d array
        f1Fight = [
            ["f1st", f1.readline()],
            ["f1agi", f1.readline()],
            ["f1dex", f1.readline()],
            ["f1int", f1.readline()],
            ["f1luk", f1.readline()]
        ]
        f2Fight = [
            ["f2st", f2.readline()],
            ["f2agi", f2.readline()],
            ["f2dex", f2.readline()],
            ["f2int", f2.readline()],
            ["f2luk", f2.readline()]
        ]

        print("Testing opponents on", statNames[test1], ", ", statNames[test2], "and ", statNames[test3], ".")
		
		# This could once again be done with another function for efficiency
		
        print("Commencing", statNames[test1], "fight.")

        f1Points = 0
        f2Points = 0

        if f1Fight[test1][1] > f2Fight[test1][1]:  # comparing their statistics for that test
            print(x, "wins!")
            f1Points += 1

        elif f2Fight[test1][1] > f1Fight[test1][1]:
            print(y, "wins!")
            f2Points += 1

        elif f1Fight[test1][1] == f2Fight[test1][1]:
            print(x, "and", y, "draw!\n No points are awarded :(")

        print("Commencing", statNames[test2], "fight.")

        if f1Fight[test2][1] > f2Fight[test2][1]:
            print(x, "wins!")
            f1Points += 1

        elif f2Fight[test2][1] > f1Fight[test2][1]:
            print(y, "wins!")
            f2Points += 1

        elif f1Fight[test2][1] == f2Fight[test2][1]:
            print(x, "and", y, "draw!\n No points are awarded :(")

        print("Commencing", statNames[test3], "fight.")

        if f1Fight[test3][1] > f2Fight[test3][1]:
            print(x, "wins!")
            f1Points += 1

        elif f2Fight[test3][1] > f1Fight[test3][1]:
            print(y, "wins!")
            f2Points += 1

        elif f1Fight[test3][1] == f2Fight[test3][1]:
            print(x, "and", y, "draw!\n No points are awarded :(")

        if f1Points > f2Points:
            print(x, "won overall!")

        elif f2Points > f1Points:
            print(y, "wins overall!")

        elif f1Points == f2Points:
            print(x, "and", y, "drew overall!")

        f1.close()
        f2.close()  # closes both

        main()

    else:
        print("One or more of these characters do not exist")
        main()


def main():  # main menu
    print(
        "\nThis program was created by Charles\n"
        "Welcome to the main menu!\n"
        "Specify the number from one of the following:\n"
        "1. Create character\n"
        "2. View character\n"
        "3. Fight characters\n"
        "4. Exit"
    )
    choice = input("Enter the number:")  # use string so it's harder to break program
	
    if choice == "1":
        charName = input("Enter the name of the character:")
        create(charName)

    elif choice == "2":
        viewChar = input("Enter the name of the character you want to view:")
        view(viewChar)

    elif choice == "3":
        char1 = input("Enter the name of the first character to fight:")
        char2 = input("Enter the name of the second character to fight:")
        fight(char1, char2)

    elif choice == "4":
        print("Bye")
        time.sleep(2)
        exit()

    else:
        print("Invalid option enter. \n '1', '2', '3' or '4' without speech marks")
        main()


main()
