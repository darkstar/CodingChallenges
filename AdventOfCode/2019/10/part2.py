import math

asteroids = []
dists = []

starbase = (27, 19)

# topological sort:
# first sort by angle of the reduced fraction
# then sort by distance
#
# ^
# |  x
# | /
# |/t
# +--------->
# t = atan2(dy, dx)
# we need the angle from straight up (y-direction)
# and to the right, so we do
# t = atan2(dx, dy)
def getdelta(x2, y2):
    dx = x2 - starbase[0]
    dy = - (y2 - starbase[1])
    dist = math.sqrt(dx * dx + dy * dy)
    # reduce fraction
    gcd = math.gcd(dx, dy)
    if gcd != 0:
        dx = dx // gcd
        dy = dy // gcd
    theta = math.atan2(dx, dy)
    if theta < 0: theta += 2 * math.pi
#    print("from {} to {}: delta = {}, theta = {}, dist = {}".format( starbase, (x2, y2), (dx, dy), theta, dist))
    return ( theta, dist, ( x2, y2 ) )

with open("input.txt", mode="r") as f:
    starmap = f.readlines()

    for y in range(len(starmap)):
        for x in range(len(starmap[y])):
            if starmap[y][x] == '#':
                asteroids.append( (x, y) )

for (x, y) in asteroids:
    if (x, y) == starbase: continue
    dists.append(getdelta(x, y))

dists.sort()

alpha = 0
pos = 0
vaporized = 0
# loop through the sorted list
while True:
    # this is the next angle to be vaporized
    asteroid = dists[pos]
    alpha = asteroid[0]
    vaporized += 1
    # check if we are done
    if vaporized == 200:
        print("result: {}".format(asteroid[2][0] * 100 + asteroid[2][1]))
        exit(1)
    # if not done, then remove the vaporized asteroid...
    dists.pop(pos)
    # ...check if it was the last one (sanity check, shouldn't happen)
    if len(dists) == 0:
        break
    # ...and skip over all that are behind it (same angle)
    while pos < len(dists) and dists[pos][0] == alpha:
        pos += 1
    # if we reached the end of the list, start again from the beginning
    if pos >= len(dists):
        dists = 0

