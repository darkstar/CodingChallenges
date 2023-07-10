import re

pos = (1, 1)
num = 0
grid = {}
pathlen = {}

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

# source point
pathlen[(1, 1)] = 0

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

count = 0
for y in range(50):
    for x in range(50):
        if pathlen[(x, y)] <= 50:
            count += 1

print(count)
