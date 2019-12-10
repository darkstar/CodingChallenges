import math

asteroids = []
maxvisible = 0
maxpos = (-1, -1)

def getdelta(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    # reduce fraction
    gcd = math.gcd(dx, dy)
    if gcd != 0:
        return (dx // gcd, dy // gcd)
    if dx == 0:
        return (0, 1 if dy > 0 else -1)
    if dy == 0:
        return (1 if dx > 0 else -1, 0)
    return (dx, dy)

with open("input.txt", mode="r") as f:
    starmap = f.readlines()

    for y in range(len(starmap)):
        for x in range(len(starmap[y])):
            if starmap[y][x] == '#':
                asteroids.append( (x, y) )

for (x, y) in asteroids:
    tmpvis = set()
    for (x2, y2) in asteroids:
        if x == x2 and y == y2:
            continue
        delta = getdelta(x, y, x2, y2)
        tmpvis.add( delta )
    if len(tmpvis) > maxvisible:
        maxvisible = len(tmpvis)
        maxpos = (x, y)

print("Maximum {} at {}".format(maxvisible, maxpos))

