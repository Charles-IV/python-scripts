from string import ascii_lowercase

#s = "abcdefghijklmnopqrstuvwxyz"
# input file
fname = input("Enter filename (including extension): ")
f = open(fname, "r")
print("reading...")
s = f.read()  # save contents of file
f.close()
s = s.lower()  # make it lowercase

# Create array to count on
count = []
for c in ascii_lowercase:
    count.append([c, 0])


# for progress bar
l = len(s)

def CreateProgressBar(barLength, max, value, start="[", end="]", block="#", emp=" ", front="", showPct=False):
    pct = value / max

    # [, block for the percentage times of barLength, front, emp (empty space) for the rest, ], then a buffer and percentage if showPct
    return "{}{}{}{}{}{}".format(start, block * int(barLength * pct), front, emp * (barLength - int(barLength * pct)), end, "{:6}%".format(round(pct * 100, 2)) if showPct else "")


# start counting
print("counting...")
#for letter in s:
for i in range(0, l):  # use index positions for progress bar
    for char in count:
        if s[i] == char[0]:
            char[1] += 1
    #out = "\r{}".format(CreateProgressBar(50, l, i, block="=", front=">", showPct=True))
    #print(out, end="")
    print("\r{:5}%".format(round(((i/l)*100), 1)), end="")  # don't show bar to make it faster


# print results
print("\n\nresults:")
for i in count:
    print("{} = {}".format(i[0], i[1]))
