def issym(grid, x, y):
    if x < 0:
        return False
    if x >= len(grid[0]):
        return False
    if y < 0:
        return False
    if y >= len(grid[0]):
        return False
    c = grid[y][x]
    if c in "0123456789.":
        return False
    return True

def hassym(grid, x, y, l):
    # check bounding box for symbols
    for xx in range(x - 1, x + l + 1):
        if issym(grid, xx, y - 1) or issym(grid, xx, y + 1):
            return True
    if issym(grid, x - 1, y) or issym(grid, x + l, y):
        return True
    return False

with open("input.txt", mode="r") as f:
    grid = [ list(x.strip()) for x in f.readlines()]

x = 0
y = 0
result = 0
while True:
    # search number
    if grid[y][x] in "0123456789":
        # we have a number. now find all digits
        num = ""
        while x < len(grid[0]) and grid[y][x] in "0123456789":
            num += grid[y][x]
            x = x + 1
        if hassym(grid, x - len(num), y, len(num)):
            result += int(num)
    else:
        # skip to next char
        x = x + 1
    # check that we did not overrun the borders
    if x >= len(grid[0]):
        y = y + 1
        x = 0
    if y >= len(grid):
        break;

print(result)
