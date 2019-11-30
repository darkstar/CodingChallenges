import re

display = [[ "." ] * 50 for x in range(6)]

def prdisplay():
    for s in display:
        print("".join(s))

with open("input.txt", mode="r") as f:
    insns = f.readlines()
    for s in insns:
        m = re.match(r"rect (\d+)x(\d+)", s)
        if m:
            w = int(m.group(1))
            h = int(m.group(2))
            for y in range(h):
                for x in range(w):
                    display[y][x] = "#"
            continue
        m = re.match(r"rotate row y=(\d+) by (\d+)", s)
        if m:
            y = int(m.group(1))
            delta = int(m.group(2))
            l = display[y]
            l = l[-delta:] + l[:-delta]
            display[y] = l
            continue
        m = re.match(r"rotate column x=(\d+) by (\d+)", s)
        if m:
            x = int(m.group(1))
            delta = int(m.group(2))
            col = list(map(lambda l: l[x], display))
            col = col[-delta:] + col[:-delta]
            for i in range(6):
                display[i][x] = col[i]
            continue
        print("invalid instruction: {}".format(s))

pixelcount = len(list(filter(lambda x: x == '#', [ x for row in display for x in row ])))
prdisplay()

