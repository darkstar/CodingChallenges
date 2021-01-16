import re

rangeregex = re.compile(r"(?P<from>\d+)-(?P<to>\d+)")
ticketregex = re.compile(r"^((\d+),)*\d+$")

validranges = []
alltickets = []

with open("input.txt", mode="r") as f:
    while True:
        l = f.readline().strip()
        if len(l) == 0:
            break
        m = rangeregex.findall(l)
        for r in m:
            validranges.append((int(r[0]), int(r[1])))

    while True:
        l = f.readline()
        if not l:
            break
        l = l.strip()
        m = ticketregex.match(l)
        if m:
            alltickets.append(list(map(int, l.split(","))))


# skip first ticket
alltickets = alltickets[1:]
error = 0
for t in alltickets:
    for v in t:
        valid = any(map(lambda x: v >= x[0] and v <= x[1], validranges))
        if not valid:
            error += v

print(error)
