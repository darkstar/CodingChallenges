import re

def calcchecksum(name):
    letters = {}
    llist = []
    for c in name:
        if c == '-': continue
        if c in letters:
            letters[c] = letters[c] + 1
        else:
            letters[c] = 1

    # convert to list of pairs
    for c in letters:
        llist.append( (c, letters[c]) )
    # sort the list
    llist.sort(key = lambda x: (-x[1], x[0]))
    # build result
    return "".join(list(map(lambda x: x[0], llist[:5])))

result = 0

with open("input.txt", mode="r") as f:
    allrooms = f.readlines()

    for room in allrooms:
        m = re.match(r"(\S+)-(\d+)\[(\w+)\]", room)
        if m is None:
            print("error: {}", room)
            exit(1)
        roomname = m.group(1)
        sectorid = int(m.group(2))
        checksum = m.group(3)
        if checksum == calcchecksum(roomname):
            result += sectorid

print(result)
