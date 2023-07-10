import re

rangeregex = re.compile(r"(?P<from>\d+)-(?P<to>\d+)")
ticketregex = re.compile(r"^((\d+),)*\d+$")

validranges = []
alltickets = []
ranges = {}

# this is probably the most complicated way to do this but it was still fun :)

with open("input.txt", mode="r") as f:
    while True:
        l = f.readline().strip()
        if len(l) == 0:
            break
        m = rangeregex.findall(l)
        if m:
            # add to ranges array
            name = l.split(":")[0]
            ranges[name] = [ (int(r[0]), int(r[1])) for r in m]
            # add to all valid ranges array
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
yourticket = alltickets[0]
alltickets = alltickets[1:]
validtickets = []
for t in alltickets:
    for v in t:
        valid = any(map(lambda x: v >= x[0] and v <= x[1], validranges))
        if not valid:
            break
    if valid:
        validtickets.append(t)

# check valid tickets
fields = list(zip(*validtickets))

def rangematch(val, rng):
    return any(map(lambda se: val >= se[0] and val <= se[1], rng))

# this will store the possible rules for each field index
possiblematches = {}
for fidx in range(len(fields)):
    possiblematches[fidx] = set()

for fidx in range(len(fields)):
    fdata = fields[fidx]
    for rule, rdata in ranges.items():
        matches = list(map(lambda v: rangematch(v, rdata), fdata))
        if all(matches):
            possiblematches[fidx].add(rule)

# now solve the possible matches, one by one
while True:
    toremove = set()
    for a, b in possiblematches.items():
        if len(b) == 1:
            toremove.add(list(b)[0])
    # if all elements have only one candidate remaining we are finished
    if len(toremove) == len(ranges):
        break
    # now remove the resolved entries
    for a in possiblematches:
        if len(possiblematches[a]) > 1:
            possiblematches[a] = possiblematches[a].difference(toremove)

# now reverse the result
indexes = { list(b)[0]: a for a, b in possiblematches.items() }

wanted = [ a for a in indexes if a.startswith("departure") ]
windex = [ indexes[a] for a in wanted ]
wvalues = [ yourticket[i] for i in windex ]

result = 1
for x in wvalues:
    result *= x

print(result)
