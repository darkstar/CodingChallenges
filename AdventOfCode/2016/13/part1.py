import re

pos = (1, 1)
num = 0
grid = {}
pathlen = {}

def printgrid(grid):
    print("   ", end='')
    for x in range(50):
        print(" " if x//10 < 1 else str(x//10), end='')
    print("")
    print("   ", end='')
    for x in range(50):
        print(x%10, end='')
    print("")
    for y in range(50):
        print("{0:2d} ".format(y), end='')
        for x in range(50):
            if (x, y) == (1, 1):
                print("A", end='')
            elif (x, y) == (31, 39):
                print("Z", end='')
            elif grid[(x, y)] == 1:
                print("#", end='')
            elif grid[(x, y)] == 2:
                print("*", end='')
            else:
                print(".", end='')
        print("")

def wall(x, y):
    global num
    wall = x*x + 3*x + 2*x*y + y + y*y
    wall = wall + num
    return bin(wall).count("1") % 2

with open("input.txt") as f:
    num = int(f.readlines()[0])

for y in range(50):
    for x in range(50):
        grid[(x, y)] = wall(x, y)
        pathlen[(x, y)] = 9999

# destination point
pathlen[(31, 39)] = 0

# A*
while True:
    changes = 0
    for y in range(50):
        for x in range(50):
            # skip walls
            if grid[(x, y)] == 1:
                continue
            # find new minimum
            values = []
            if x > 0:
                values.append(pathlen[(x - 1, y)] + 1)
            if x < 49:
                values.append(pathlen[(x + 1, y)] + 1)
            if y > 0:
                values.append(pathlen[(x, y - 1)] + 1)
            if y < 49:
                values.append(pathlen[(x, y + 1)] + 1)
            new = min(*values)
            old = pathlen[(x, y)]
            if new < old:
                pathlen[(x, y)] = new
                changes += 1
    if changes == 0:
        break

print(pathlen[(1, 1)])

debug = 0

if debug:
    # mark path
    pos = (1, 1)
    while pos != (31, 39):
        cur = pathlen[pos]
        (x, y) = pos
        p1 = pathlen[(x - 1, y)] if x > 0 else 9999
        p2 = pathlen[(x + 1, y)] if x < 49 else 9999
        p3 = pathlen[(x, y - 1)] if y > 0 else 9999
        p4 = pathlen[(x, y + 1)] if y < 49 else 9999
        print("pos: {} ({}), dirs={},{},{},{}".format(pos, cur, p1, p2, p3, p4))
        if p1 == min(p1, p2, p3, p4):
            newpos = (x - 1, y)
        elif p2 == min(p1, p2, p3, p4):
            newpos = (x + 1, y)
        elif p3 == min(p1, p2, p3, p4):
            newpos = (x, y - 1)
        else:
            newpos = (x, y + 1)
        grid[newpos] = 2
        if (pos == newpos):
            print("stuck")
            break
        pos = newpos

        printgrid(grid)
