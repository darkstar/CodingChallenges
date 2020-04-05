with open("input.txt") as f:
    steps = int(f.readline().strip())

zeropos = 0
left = 0
right = 0
pos = 0
lastvalue = -1

for x in range(1, 50000000):
    # step ahead
    pos = (pos + steps) % x
    # increas front/back tails
    if pos <= zeropos:
        left += 1
    else:
        right += 1
    # "insert" new value
    newpos = pos + 1
    if newpos == zeropos + 1:
        lastvalue = x
    # new "start" position
    pos = newpos

print(lastvalue)
