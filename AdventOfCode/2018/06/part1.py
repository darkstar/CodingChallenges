import re
import random

field = [[0 for x in range(500)] for y in range(500)]
coords = []
infinite = {}

def mdist(p1, p2):
  return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])

# warning: this is a braindead straight-forward implementation ;-)

with open('input.txt', mode='r') as f:
  lines = f.readlines()

  for line in lines:
    m = re.match('(\d+),\s*(\d+)', line)
    x, y = int(m.groups()[0]), int(m.groups()[1])
    coords.append( (x,y) )

  for y in range(500):
    for x in range(500):
      distances = list(map(lambda p: mdist(p, (x, y)), coords))
      mindist = min(distances)
      minidx = distances.index(mindist)
      # check if the distance is unique
      if distances.count(mindist) == 1:
        field[x][y] = minidx + 1

  # find infinitely large areas (those with at least one border pixel)
  for x in range (500):
    if field[x][0] != 0:
      infinite[field[x][0]] = 1
    if field[x][500-1] != 0:
      infinite[field[x][500-1]] = 1
    if field[0][x] != 0:
      infinite[field[0][x]] = 1
    if field[500-1][x] != 0:
      infinite[field[500-1][x]] = 1

  noninfinite = list(filter(lambda k: k > 0 and k not in infinite.keys(), [x for x in range(len(coords))]))
  sizes = {}
  for n in noninfinite:
    size = len(list(filter(lambda p: n == p, [k for row in field for k in row])))
    sizes[n] = size

  maxsize = max(sizes, key = lambda k: sizes[k])
  print(sizes[maxsize])

  exit(0)

  # debug: save the area as image
  pal = [ [random.randint(0, 255) for x in range (3)] for y in range(64) ]

  with open('image.ppm', mode='w') as o:
    o.write("P3 500 500 255\n")
    for y in range(500):
      for x in range(500):
        o.write("{} {} {} ".format(pal[field[x][y]][0], pal[field[x][y]][1], pal[field[x][y]][2]))
      o.write('\n')
