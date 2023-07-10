import re
from functools import reduce

p = re.compile('(\d+),(\d+) -> (\d+),(\d+)')

def parse(line):
  result = p.match(line)
  if result:
    return ( int(result.group(1)), int(result.group(2)), int(result.group(3)), int(result.group(4)))
  return None

with open("input.txt", mode="r") as f:
  lines = list(map(parse, [ l.strip() for l in f.readlines() ]))

# filter only horizontal or vertical lines
hlines = list(filter(lambda l: l[1] == l[3], lines))
vlines = list(filter(lambda l: l[0] == l[2], lines))

field = {}

for l in hlines:
  y = l[1]
  for x in range(min(l[0], l[2]), max(l[0], l[2]) + 1):
    if (x, y) in field:
      field[(x, y)] = field[(x, y)] + 1
    else:
      field[(x, y)] = 1

for l in vlines:
  x = l[0]
  for y in range(min(l[1], l[3]), max(l[1], l[3]) + 1):
    if (x, y) in field:
      field[(x, y)] = field[(x, y)] + 1
    else:
      field[(x, y)] = 1

sol = reduce(lambda x, value: x if value < 2 else x + 1, field.values(), 0)

print(sol)

