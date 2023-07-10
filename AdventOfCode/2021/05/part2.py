import re
from functools import reduce

p = re.compile('(\d+),(\d+) -> (\d+),(\d+)')

def parse(line):
  result = p.match(line)
  if result:
    return ( int(result.group(1)), int(result.group(2)), int(result.group(3)), int(result.group(4)))
  return None

def drawpoint(p, field):
  if p in field:
    field[p] = field[p] + 1
  else:
    field[p] = 1

def drawline(l, field):
  if l[0] == l[2]:
    dx = 0
  elif l[0] < l[2]:
    dx = 1
  else:
    dx = -1

  if l[1] == l[3]:
    dy = 0
  elif l[1] < l[3]:
    dy = 1
  else:
    dy = -1

  p = (l[0], l[1])
  end = (l[2], l[3])
  while p != end:
    drawpoint(p, field)
    p = (p[0] + dx, p[1] + dy)
  drawpoint(p, field)

with open("input.txt", mode="r") as f:
  lines = list(map(parse, [ l.strip() for l in f.readlines() ]))

field = {}

for l in lines:
  drawline(l, field)

sol = reduce(lambda x, value: x if value < 2 else x + 1, field.values(), 0)

print(sol)

