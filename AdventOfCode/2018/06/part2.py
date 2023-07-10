import re
import random

coords = []
areasize = 0

def mdist(p1, p2):
  return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])

with open('input.txt', mode='r') as f:
  lines = f.readlines()

  for line in lines:
    m = re.match('(\d+),\s*(\d+)', line)
    x, y = int(m.groups()[0]), int(m.groups()[1])
    coords.append( (x,y) )

  for y in range(500):
    for x in range(500):
      distances = list(map(lambda p: mdist(p, (x, y)), coords))
      totaldist = sum(distances)
      if totaldist < 10000:
        areasize += 1

  print(areasize)

