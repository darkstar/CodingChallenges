import re

with open("input.txt") as f:
    df = f.readlines()[2:]

noderegex = re.compile(r'/dev/grid/node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T\s+(\d+)%')

nodes = {}
dimension = (0, 0)

for line in df:
    m = noderegex.match(line)
    if m:
        x = int(m.group(1))
        y = int(m.group(2))
        nodes[ (x, y) ] = { "x": x, "y": y, "size": int(m.group(3)), 
            "used": int(m.group(4)), "avail": int(m.group(5)), "pct": int(m.group(6)) }
        if x > dimension[0]:
            dimension = (x, dimension[1])
        if y > dimension[1]:
            dimension = (dimension[0], y)
        pass
    else:
        print("Invalid line: {}".format(line))
        exit(1)

target = nodes[ (dimension[0], 0) ]
datasize = target["used"]

# print("target: {}".format(target))
# print("data size: {}".format(datasize))

# find nodes with at least 70tb free
freenode = [ x for x in nodes.values() if x["avail"] >= datasize ][0]
# print("node with enough space: {}".format(freenode))

# find full nodes
minsize = min(map(lambda x: x["size"], nodes.values()))
# print("minimum size disk: {}".format(minsize))
fullnodes = [ x for x in nodes.values() if x["used"] > minsize ]
# print("full nodes: {}".format(list(map(lambda n: (n["x"], n["y"]), fullnodes))))

# move the "largenode" to the left of the target (X, 0)
# this requires A* or similar (69 steps in my case)

# build matrix from nodes (9999 = wall, -1 = not yet visited, 0 = start)
maze = [ [ 9999 if nodes[(x, y)] in fullnodes else -1 for x in range(dimension[0] + 1) ] for y in range(dimension[1] + 1) ]
# target node for pathfinding (left of the real target)
maze[0][dimension[0]-1] = 0

while True:
    changes = 0
    # copy the maze
    newmaze = [ [ maze[y][x] for x in range(dimension[0] + 1)] for y in range(dimension[1] + 1)]
    for y in range(dimension[1] + 1):
        for x in range(dimension[0] + 1):
            # skip walls and parts of the path that has been done already
            if maze[y][x] != -1:
                continue
            neighbors = []
            if (x > 0): neighbors.append(maze[y][x-1])
            if (x < dimension[0]): neighbors.append(maze[y][x+1])
            if (y > 0): neighbors.append(maze[y-1][x])
            if (y < dimension[1]): neighbors.append(maze[y+1][x])
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

pathsteps = maze[freenode["y"]][freenode["x"]]
# print("taking {} steps to move into position".format(pathsteps))

# then, repeat: right, down, left, left, up
# until target is at (1,0) -> X-1 * 5 steps (32 * 5 steps here)
shiftsteps = (dimension[0] - 1) * 5
# print("shifting target left {} times -> {} steps".format(dimension[0]-1, shiftsteps))
# then finish with "right" -> 1 step
totalsteps = pathsteps + shiftsteps + 1
# verified via https://codepen.io/anon/pen/BQEZzK/

print(totalsteps)
