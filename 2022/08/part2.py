from itertools import takewhile
from math import prod

with open("input.txt", mode="r") as f:
    grid = [ list(map(int, x.strip())) for x in f.readlines() ]

def dist(l):
    r = list(takewhile(lambda n: n < l[0], l[1:]))
    if len(r) == len(l) - 1:
        return len(r)
    return len(r) + 1

def score(x):
    return prod(map(dist, x))

result = 0

for y in range(len(grid)):
    for x in range(len(grid[0])):
        # extract row and column
        r = grid[y]
        c = [ g[x] for g in grid ]
        # extract left, right, up, down lists
        left = r[:x + 1][::-1]
        right = r[x:]
        up = c[:y + 1][::-1]
        down = c[y:]

        vd = score([left, right, up, down])
        if vd > result:
            result = vd

print(result)
