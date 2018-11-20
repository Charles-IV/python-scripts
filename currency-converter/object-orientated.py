curr = []  # array of currencies


class Currency:
    def __init__(self, name, value):  # name, value of 1 GBP -> it
        self.name = name
        self.value = value

    def __str__(self):  # output the name of the currency
        return self.name

    def __float__(self):  # output  exact value compared to GBP
        return self.value

    def toBase(self, inp):  # convert it to GBP
        return inp * (1/self.value)

    def fromBase(self, inp):  # convert it from GBP
        return inp * self.value


#########################
# INITIALISE CURRENCIES #
#########################

curr.append(Currency("GBP", 1.0))  # add GBP
curr.append(Currency("USD", 1.28436))  # USD
curr.append(Currency("YEN", 144.30915))  # YEN
curr.append(Currency("EUR", 1.12338))  # EUR


############################################
# START PROCESS OF GETTING STUFF FROM USER #
############################################

print("Enter currency to convert from:")
for i in range(1, len(curr)+1):
    print("{}. {}".format(i, str(curr[i-1])))

currFrom = curr[int(input("\n>"))-1]  # NO I CBA VALIDATE, I WANNA GO FAST AND GET ONTO OOP


print("Do you want to convert to:\n")
for i in range(1, len(curr)+1):
    print("{}. {}".format(i, str(curr[i-1])))

currTo = curr[int(input("\n>"))-1]  # NO I CBA VALIDATE, I WANNA GO FAST AND GET ONTO OOP

inp = int(input("\nEnter amount:\n>"))

# convert input to GBP, then the currency they asked for
print("{0} {1} in {2}:\n{3} {2}".format(inp, str(currFrom), str(currTo), round(currTo.fromBase(currFrom.toBase(inp)), 2)))

