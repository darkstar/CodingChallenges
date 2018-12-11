grid_serial = 0
grid = [[0 for y in range(300)] for x in range(300)]

best_coord = (0, 0)
best_sum = 0

with open('input.txt', mode='r') as f:
    grid_serial = int(f.readlines()[0].rstrip())

def subsum(x, y, size):
    level = 0
    for yy in range(y, y + size):
        for xx in range(x, x + size):
            level += grid[xx][yy]
    return level

# initialize grid
for y in range(300):
    for x in range(300):
        xcoord = x + 1
        ycoord = y + 1
        rackid = xcoord + 10
        powerlevel = (rackid * ycoord + grid_serial) * rackid
        powerlevel = (powerlevel % 1000) // 100
        grid[x][y] = powerlevel - 5

# find best match
for y in range(300 - 2):
    for x in range(300 - 2):
        level = subsum(x, y, 3)

        if level > best_sum:
            best_sum = level
            best_coord = (x + 1, y + 1)

print(best_coord)

