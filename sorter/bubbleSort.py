"""
Charles IV
Bubble Sort
Prints every step, notifies you of a new pass
"""

names = input("Enter list, seperated by commas and no spaces.\n> ").split(",")
order = input("Order list ascending from smallest to largest? [Y/n]: ")

if order == "n":
    order = ">"
else:
    order = "<"


def bubbleSort(arr, order):
    passNo = 1
    lArr = len(arr)
    sortDone = False
    sortHappened = False  # if something was moved
    while not sortDone:
        print("Pass {} started".format(passNo))  # notify it's starting a new pass
        swaps = 0
        print(arr)  # print what array starts as on each pass
        for i in range(1, lArr-(passNo-1)):  # 1 pass through array, don't check sorted numbers
            if eval(arr[i] + order + arr[i-1]):  # if later position should be before earlier:
                temp = arr[i-1]  # save earlier to temporary var
                arr[i-1] = arr[i]  # replace earlier with later
                arr[i] = temp  # # replace later with earlier
                swaps += 1
                print(arr)
            else:
                print(arr)
        
        print("Pass {} done with {} comparisons and {} swap{}".format(passNo, (lArr-(passNo-1)-1), swaps, "" if swaps == 1 else "s"))

        # after the pass
        if swaps == 0:  # if nothing was moved
            print("Done in {} passes".format(passNo))
            sortDone = True  # stop looping
        passNo += 1


bubbleSort(names, order)

"""
Please excuse any inefficiency. I've got this working, and just remembered to remove all of the test prints I had.
(originally I forgot to add line 10)
"""
