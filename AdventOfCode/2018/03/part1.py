import re

fabric = [[0 for x in range(1000)] for y in range(1000)]

with open('input.txt', mode='r') as f:
  lines = f.readlines()

  for line in lines:
    m = re.match(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', line)
    x = int(m.groups()[1])
    y = int(m.groups()[2])
    w = int(m.groups()[3])
    h = int(m.groups()[4])

    for yy in range(y, y+h):
      for xx in range(x, x+w):
        fabric[xx][yy] += 1

print('Overlaps:', len(list(filter(lambda x: x > 1, [x for column in fabric for x in column]))))
