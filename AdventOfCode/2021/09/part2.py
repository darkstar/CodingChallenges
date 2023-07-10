from functools import reduce

with open("input.txt", mode="r") as f:
  themap = [ x.strip() for x in f.readlines() ]

#themap = ["2199943210","3987894921","9856789892","8767896789","9899965678"]

xsize = len(themap[0])
ysize = len(themap)

lowpoints = []

for y in range(ysize):
  for x in range(xsize):
    neighbors = []
    height = int(themap[y][x])
    if x > 0:
      neighbors.append(int(themap[y][x-1]))
    if x < xsize - 1:
      neighbors.append(int(themap[y][x+1]))
    if y > 0:
      neighbors.append(int(themap[y-1][x]))
    if y < ysize - 1:
      neighbors.append(int(themap[y+1][x]))
    low = all(map(lambda h: height < h, neighbors))
    if low:
      lowpoints.append((x, y))

sizes = []

# suboptimal.
# this could be done in one iteration but I'm too lazy right now

for p in lowpoints:
  fmap = [ [ 0 ] * xsize for y in range(ysize) ]
  fmap[p[1]][p[0]] = 1
  # floodfill
  while True:
    changed = 0
    for y in range(ysize):
      for x in range(xsize):
        # skip 9-fields
        if themap[y][x] == '9':
          continue
        # skip already set points
        if fmap[y][x] != 0:
          continue
        if (x > 0 and fmap[y][x-1] == 1) or (x < xsize - 1 and fmap[y][x+1]) or \
           (y > 0 and fmap[y-1][x] == 1) or (y < ysize - 1 and fmap[y+1][x]):
           changed = changed + 1
           fmap[y][x] = 1
    if changed == 0:
      break

  size = len([ x for y in fmap for x in y if x == 1])
  sizes.append(size)

big = sorted(sizes)[-3:]
print(big[0] * big[1] * big[2])
