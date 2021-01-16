def say(state, n):
    return 0

lastnum = -1
prevs = {}
turn = 0

with open("input.txt", mode="r") as f:
    starting = f.readline().strip().split(",")
    for n in range(len(starting)):
        if lastnum >= 0:
            prevs[lastnum] = n
        turn += 1
        lastnum = int(starting[n])

while turn < 30000000:
    last = lastnum
    if lastnum in prevs:
        age = turn - prevs[last]
        lastnum = age
    else:
        lastnum = 0
    prevs[last] = turn
    turn += 1

print(lastnum)
