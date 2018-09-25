no = int(input("Enter number to work out factorial of: "))


def recursive_factorial(n, fact=1):
    # fact = 1  # number to add to
    fact *= n
    n -= 1
    print("fact: {}, n = {}".format(fact, n))
    if n > 1:
        fact = recursive_factorial(n, fact)

    return fact

print(recursive_factorial(no))
