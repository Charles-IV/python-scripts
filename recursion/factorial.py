no = int(input("Enter number to work out factorial of: "))


def recursive_factorial(n, fact=1):
    # fact = 1  # number to add to
    fact *= n  # does factorial calculation
    n -= 1  # prepare for next recursion
    #print("fact: {}, n = {}".format(fact, n)) - test for debugging
    if n > 1:  # keep repeating until it gets too low
        fact = recursive_factorial(n, fact)  # pass variable back to output correct value

    return fact  # return to output or lower level of recursion to output

print(recursive_factorial(no))
