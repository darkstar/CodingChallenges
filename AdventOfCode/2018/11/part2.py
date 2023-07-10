grid_serial = 0
grid = [[0 for y in range(300)] for x in range(300)]

best_coord = (0, 0)
best_sum = 0
best_size = 0

sumlevels = {}
#sumlevels_new = {}

with open('input.txt', mode='r') as f:
    grid_serial = int(f.readlines()[0].rstrip())

def subsum(x, y, size):
    level = 0

    if size % 2 == 0:
        # add from four squares
        hsize = size // 2
        level = sumlevels[(x, y, hsize)] + sumlevels[(x + hsize, y, hsize)] + \
                sumlevels[(x, y + hsize, hsize)] + sumlevels[(x + hsize, y + hsize, hsize)]
    else:
        # get previous sum of rectangle with size 1 smaller
        if (x, y, size - 1) in sumlevels:
            level = sumlevels[(x, y, size - 1)]

        # add right and lower border
        for xx in range(size):
            level += grid[x + xx][y + size - 1]
            level += grid[x + size - 1][y + xx]

        # remove doubly-counted corner
        level -= grid[x + size - 1][y + size - 1]

    # store for later
    sumlevels[(x, y, size)] = level

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
for size in range(1, 300):
    print("Size {}, best so far: {},{},{}".format(size, best_coord[0], best_coord[1], best_size))
    for y in range(300 - (size - 1)):
        for x in range(300 - (size - 1)):
            level = subsum(x, y, size)

            if level > best_sum:
                best_sum = level
                best_coord = (x + 1, y + 1)
                best_size = size
#    sumlevels = sumlevels_new
#    sumlevels_new = {}

print("{},{},{}".format(best_coord[0], best_coord[1], best_size))

