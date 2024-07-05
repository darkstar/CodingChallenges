with open("input.txt", mode="r") as f:
    grid = [ list(x.strip()) for x in f.readlines()]

x = 0
y = 0
nums = {}

while True:
    # search all numbers
    if grid[y][x] in "0123456789":
        # we have a number. now find all digits
        num = ""
        while x < len(grid[0]) and grid[y][x] in "0123456789":
            num += grid[y][x]
            x = x + 1
        # store the number in a dict for all grid positions it occupies
        for xx in range(x - len(num), x):
            nums[(xx, y)] = (x - len(num), y, int(num))

    else:
        # skip to next char
        x = x + 1
    # check that we did not overrun the borders
    if x >= len(grid[0]):
        y = y + 1
        x = 0
    if y >= len(grid):
        break;

# step 2: find all gears
result = 0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == "*":
            # find numbers around the position
            foundnums = set()
            for xx in range(x - 1, x + 2):
                for yy in range(y - 1, y + 2):
                    if (xx, yy) in nums:
                        foundnums.add(nums[(xx,yy)])
            # check if we have exactly 2 numbers
            if len(foundnums) == 2:
                ratio = 1
                for e in foundnums:
                    ratio *= e[2]
                result += ratio

print(result)
