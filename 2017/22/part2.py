# direction. 0 = up, 1 = right, 2 = down, 3 = left
dirs = [ (0, 1), (1, 0), (0, -1), (-1, 0) ]

with open("input.txt") as f:
    startmap = f.readlines()

# for testing
#startmap = [ "..#", "#..", "..." ]

xsize = len(startmap[0])
ysize = len(startmap)

mid = ((xsize - 1) // 2, (ysize - 1) // 2)

# build node map
# "#": infected
# "F": flagged
# "W": weakened
nodes = {}

for y in range(ysize):
    for x in range(xsize):
        if startmap[y][x] == "#":
            nodes[ (x - mid[0], mid[1] - y) ] = "#"

pos = (0, 0)
d = 0
infections = 0

for step in range(10000000):
    # 1 - check if node is infected, and turn accordingly
    if not pos in nodes:
        # turn left if clean
        d = (d - 1) % 4
    elif nodes[pos] == "W":
        # no turn if weakened
        pass
    elif nodes[pos] == "F":
        # reverse if flagged
        d = (d + 2) % 4
    else:
        # turn right if infected
        d = (d + 1) % 4

    # 2 - change state of the node
    if not pos in nodes:
        # clean nodes -> weakened
        nodes[pos] = "W"
    elif nodes[pos] == "W":
        # weakened nodes become infected
        infections += 1
        nodes[pos] = "#"
    elif nodes[pos] == "#":
        # infected nodes become flagged
        nodes[pos] = "F"
    else:
        # flagged nodes become clean
        del nodes[pos]

    # 3 - move in the new direction
    pos = ( pos[0] + dirs[d][0], pos[1] + dirs[d][1] )

print(infections)
