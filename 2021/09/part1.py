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

risklevels = list(map(lambda p: int(themap[p[1]][p[0]]) + 1, lowpoints))

totalrisk = reduce(lambda a, b: a + b, risklevels, 0)

print(totalrisk)
