import re

fabric = [[0 for x in range(1000)] for y in range(1000)]

with open('input.txt', mode='r') as f:
  lines = f.readlines()
  goodclaims = {}

  for line in lines:
    m = re.match(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', line)
    claim = int(m.groups()[0])
    x = int(m.groups()[1])
    y = int(m.groups()[2])
    w = int(m.groups()[3])
    h = int(m.groups()[4])
    goodclaims[claim] = True

    for yy in range(y, y+h):
      for xx in range(x, x+w):
        if fabric[xx][yy] != 0:
          goodclaims[fabric[xx][yy]] = False
          goodclaims[claim] = False
        fabric[xx][yy] = claim

print("Only non-overlapping claim:", list(filter(lambda x: x[1], goodclaims.items()))[0][0])

