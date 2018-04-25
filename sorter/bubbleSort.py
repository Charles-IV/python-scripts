"""
Charles IV
Bubble Sort
Prints every step, notifies you of a new pass
"""

names = ["Li", "N", "Et", "M", "Lu", "O", "A", "Lo", "J", "El"]


def bubbleSort(arr):
    lArr = len(arr)
    sortDone = False
    sortHappened = False  # if something was moved
    while not sortDone:
        print("Pass")  # notify it's starting a new pass
        sortHappened = False
        for i in range(1, lArr):  # 1 pass through array
            if arr[i] < arr[i-1]:  # if later position should be before earlier:
                temp = arr[i-1]  # save earlier to temporary var
                arr[i-1] = arr[i]  # replace earlier with later
                arr[i] = temp  # # replace later with earlier
                sortHappened = True
                print(arr)
            else:
                print(arr)

        # after the pass
        if sortHappened == False:  # if nothing was moved
            print("Done")
            sortDone = True  # stop looping


bubbleSort(names)

"""
Please excuse any inefficiency. I've got this working, and just remembered to remove all of the test prints I had.
(originally I forgot to add line 10)
"""