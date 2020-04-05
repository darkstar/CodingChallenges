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
infected = {}

for y in range(ysize):
    for x in range(xsize):
        if startmap[y][x] == "#":
            infected[ (x - mid[0], mid[1] - y) ] = True

pos = (0, 0)
d = 0
infections = 0

for step in range(10000):
    # 1 - check if node is infected, and turn accordingly
    if pos in infected:
        d = (d + 1) % 4
    else:
        d = (d - 1) % 4

    # 2 - clean node if it is infected
    if pos in infected:
        del infected[pos]
    else:
        infected[pos] = True
        infections += 1

    # 3 - move forward
    pos = ( pos[0] + dirs[d][0], pos[1] + dirs[d][1] )

print(infections)
