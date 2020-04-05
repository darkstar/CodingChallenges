import math

def ulam(num):
    # the layer we are in
    layer = int((math.sqrt(num - 1) + 1) / 2)
    # how "long" is each layer?
    length = 8 * layer
    # which number starts the cycle?
    first = (2 * layer - 1)**2 + 1
    # in what "sector" are we (right, up, left, down), i.e. (0, 1, 2, 3)
    sector = int(4 * (num - first) / length)
    # how far are we along the sector?
    sectorleg = (num - first) % (2 * layer)
    # where the first number in the cycle is
    pos = (layer, layer)
    # fix up by walking around the circle
    sectorstarts = [ (layer, -layer), (layer, layer), (-layer, layer), (-layer, -layer) ]
    pos = sectorstarts[sector]
    if sector == 0:
        return (pos[0], pos[1] + sectorleg + 1)
    elif sector == 1:
        return (pos[0] - sectorleg - 1, pos[1])
    elif sector == 2:
        return (pos[0], pos[1] - sectorleg - 1)
    else:
        return (pos[0] + sectorleg + 1, pos[1])

with open("input.txt") as f:
    target = int(f.readline().strip())

values = { (0, 0): 1 }

num = 2
while True:
    (x, y) = ulam(num)
    # find neighbor sum
    nsum = 0
    if (x - 1, y - 1) in values: nsum += values[ (x - 1, y - 1) ]
    if (x - 1, y) in values: nsum += values[ (x - 1, y) ]
    if (x - 1, y + 1) in values: nsum += values[ (x - 1, y + 1) ]
    if (x, y - 1) in values: nsum += values[ (x, y - 1) ]
    if (x, y + 1) in values: nsum += values[ (x, y + 1) ]
    if (x + 1, y - 1) in values: nsum += values[ (x + 1, y - 1) ]
    if (x + 1, y) in values: nsum += values[ (x + 1, y) ]
    if (x + 1, y + 1) in values: nsum += values[ (x + 1, y + 1) ]
    # store
    values[ (x, y) ] = nsum
    if nsum > target:
        print(nsum)
        break

    num += 1
