with open("input.txt", mode="r") as f:
    grid = [ list(map(int, x.strip())) for x in f.readlines() ]

def ascending(l):
    if len(l) <= 1:
        return True
    a, r = l[0], max(l[1:])
    return a > r

def visible(x):
    return any(map(ascending, x))

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
        if visible([ left, right, up, down ]):
            result += 1

print(result)
