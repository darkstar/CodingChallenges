import math

def prod(l):
    return math.prod(l)

with open("input.txt", mode="r") as f:
    grid = [[int(x) for x in y.strip().split(" ")] for y in f.readlines() if len(y)>1]

p = 0

# horizontal
for y in range(20):
    for x in range(17):
        n = grid[y][x:x + 4]
        p = max(p, prod(n))
# vertical
for x in range(20):
    for y in range(17):
        n = [grid[y+c][x] for c in range(4)]
        p = max(p, prod(n))
# diagonal 1
for y in range(17):
    for x in range(17):
        n = [grid[y + c][x + c] for c in range(4)]
        p = max(p, prod(n))
# diagonal 2
for y in range(17):
    for x in range(19, 2, -1):
        n = [grid[y + c][x - c] for c in range(4)]
        p = max(p, prod(n))

print(p)
