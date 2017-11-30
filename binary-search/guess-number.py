"""
Charles IV
Guessing your number
Here I used the binary search algorithm to guess the users number between 1 and 100
"""


def search(low, high):
    print(low, high)
    # total = int(high - low)
    midpoint = int((high + low) / 2)
    print(midpoint)
    answer = input("H, L or G?")
    if answer == "G":
        exit()
    elif answer == "H":
        search(low, midpoint)
    elif answer == "L":
        search(midpoint, high)

print("Think of a number between 1 and 100\nI will guess it, press H for to high, L for too low or G for got it")
search(0, 100)
