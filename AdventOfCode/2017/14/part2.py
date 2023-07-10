import functools
import operator

with open("input.txt") as f:
    prefix = f.readline().strip()

onebits = [ 0, 1, 1, 2, 1, 2, 2, 3,
            1, 2, 2, 3, 2, 3, 3, 4 ]

def knothash(s):
    pos = 0
    skipsize = 0
    lst = [ x for x in range(256) ]
    steps = list(map(ord, s)) + [ 17, 31, 73, 47, 23 ]
    # calculate 64 rounds for the sparse hash
    for rnd in range(64):
        for s in steps:
            # start swapping from p1 to p2
            p1 = pos
            p2 = pos + s - 1
            while p2 > p1:
                # swap p1 and p2, and move them
                tmp = lst[p1 % len(lst)]
                lst[p1 % len(lst)] = lst[p2 % len(lst)]
                lst[p2 % len(lst)] = tmp
                p1 += 1
                p2 -= 1
            pos = (pos + s + skipsize) % len(lst)
            skipsize += 1

    densehash = []
    
    # reduce to dense hash
    for block in range(16):
        sublst = lst[block * 16:(block + 1)*16]
        densehash.append("{0:02x}".format(functools.reduce(operator.xor, sublst)))

    return "".join(densehash)

h = knothash("{}-{}".format(prefix, 0))
maze = [ list("".join(list(map(lambda x: "{0:04b}".format(int(x, 16)), knothash("{}-{}".format(prefix, y)))))) for y in range(128) ]

groups = 0
while True:
    # find next 1-bit, i.e. used block
    used = None
    for y in range(128):
        for x in range(128):
            if maze[y][x] == "1":
                used = (x, y)
                break
    # if none found, we are finished
    if not used:
        break
    # we found another group...
    groups += 1
    # iterate through all adjacent blocks, marking them "free"
    queue = set()
    queue.add( used )
    while len(queue) > 0:
        (x, y) = queue.pop()
        maze[y][x] = "0"
        # check neighbors and add them
        if x > 0 and maze[y][x - 1] == "1":
            queue.add( (x - 1, y) )
        if x < 127 and maze[y][x + 1] == "1":
            queue.add( (x + 1, y) )
        if y > 0 and maze[y - 1][x] == "1":
            queue.add( (x, y - 1) )
        if y < 127 and maze[y + 1][x] == "1":
            queue.add( (x, y + 1) )

print(groups)
