import re
import copy
import itertools

def pathfind(originalmaze, startx, starty):
    # make a copy just to be safe
    maze = copy.deepcopy(originalmaze)
    xsize = len(maze[0])
    ysize = len(maze)
    # start condition
    maze[starty][startx] = 0
    while True:
        changes = 0
        # copy the maze
        newmaze = copy.deepcopy(maze)
        for y in range(ysize):
            for x in range(xsize):
                # skip walls and parts of the path that has been done already
                if maze[y][x] != -1:
                    continue
                neighbors = []
                if (x > 0): neighbors.append(maze[y][x-1])
                if (x < xsize - 1): neighbors.append(maze[y][x+1])
                if (y > 0): neighbors.append(maze[y-1][x])
                if (y < ysize - 1): neighbors.append(maze[y+1][x])
                # remove all -1's from neighbor list
                neighbors = list(filter(lambda x: x >= 0 and x < 9999, neighbors))
                if len(neighbors) == 0:
                    continue
                newval = min(neighbors) + 1
                newmaze[y][x] = newval
                changes += 1
        maze = newmaze
        # finish when the whole map is filled
        if changes == 0: break
    return maze

with open("input.txt") as f:
    textmaze = f.readlines()

positions = {}
ysize = len(textmaze)
xsize = len(textmaze[0].strip())

# extract positions
for y in range(ysize):
    line = textmaze[y].strip()
    for x in range(xsize):
        if line[x] in "0123456789":
            positions[int(line[x])] = ( x, y )

# build searchable maze
maze = [ [ 999999 if textmaze[y][x] == "#" else -1 for x in range(xsize) ] for y in range(ysize) ]

distancemap = {}
# print("building distance map, please wait")

# build distance map
for p in positions:
    p1 = positions[p]
    distmaze = pathfind(maze, p1[0], p1[1])
    for q in positions:
        p2 = positions[q]
        dist = distmaze[p2[1]][p2[0]]
        distancemap[ (p, q) ] = dist

targets = list(range(max(positions) + 1))[1:]
# print("Targets are {}".format(targets))

paths = list(itertools.permutations(targets))
# print("Checking {} different paths...".format(len(paths)))

shortestpath = 999999999

for path in paths:
    totaldist = 0
    pos = 0
    for step in path:
        totaldist += distancemap[ (pos, step) ]
        pos = step
    totaldist += distancemap[ (pos, 0) ]
    if totaldist < shortestpath:
        shortestpath = totaldist
        # print("New shortest path of length {}: {}".format(shortestpath, ( 0, ) + path))

print(shortestpath)
