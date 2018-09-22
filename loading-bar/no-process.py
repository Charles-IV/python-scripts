from time import sleep


def CreateProgressBar(barLength, max, value, start="[", end="]", block="#", emp=" ", front="", showPct=False):
    pct = value / max

    # [, block for the percentage times of barLength, front, emp (empty space) for the rest, ], then a buffer and percentage if showPct
    return "{}{}{}{}{}{}".format(start, block * int(barLength * pct), front, emp * (barLength - int(barLength * pct)), end, "{:6}%".format(round(pct * 100, 2)) if showPct else "")


progress = 0.00

while progress <= 100.00:
    print("\r{}".format(CreateProgressBar(50, 100, progress, block="=", front=">", showPct=True)), end="")
    # \r is like \n but stays on the same line (replacing it)

    progress += 0.01
    #sleep(0.01) - you will probably want this on a good comupter
