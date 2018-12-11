grid = [[0 for y in range(100)] for x in range(100)]

def printgrid(g):
    for y in range(100):
        l = "".join([str(grid[x][y]) for x in range(100)])
        print(l)

def l(grid, x, y):
    if (x, y) in [(0, 0), (0,99), (99,0), (99,99)]: return 1
    if x < 0 or y < 0 or x >= 100 or y >= 100: return 0
    return grid[x][y]

with open('input.txt', mode='r') as f:
    lines = f.readlines()
    for y in range(100):
        for x in range(100):
            grid[x][y] = 1 if lines[y][x] == '#' else 0

for step in range(100):
    newgrid = [[0 for y in range(100)] for x in range(100)]

    for y in range(100):
        for x in range(100):
            if (x, y) in [(0, 0), (0,99), (99,0), (99,99)]:
                newgrid[x][y] = 1
                continue

            neighbors = l(grid, x-1, y-1) + l(grid, x-1, y) + l(grid, x-1, y+1) \
                    + l(grid, x, y-1) + l(grid, x, y+1) \
                    + l(grid, x+1, y-1) + l(grid, x+1, y) + l(grid, x+1, y+1)
            if l(grid, x, y) == 1:
                newgrid[x][y] = 1 if neighbors in [2, 3] else 0
            if l(grid, x, y) == 0:
                newgrid[x][y] = 1 if neighbors == 3 else 0

    grid = newgrid

print(sum([x for row in grid for x in row]))
