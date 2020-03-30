import re

discs = []

with open("input.txt") as f:
    for l in f.readlines():
        m = re.match(r'Disc #(\d+) has (\d+) positions; at time=0, it is at position (\d+).', l)
        if m:
            discs.append({"disc": int(m.group(1)), "size": int(m.group(2)), "pos": int(m.group(3))})

discs.append({"disc": len(discs) + 1, "size": 11, "pos": 0})

print(discs)

t = 0

while True:
    res = []
    for x in discs:
        # starting at time t, disc X takes x steps to reach the destination
        res.append((x["pos"] + t + x["disc"]) % x["size"])

    if sum(res) == 0:
        print(t)
        break

    t += 1
