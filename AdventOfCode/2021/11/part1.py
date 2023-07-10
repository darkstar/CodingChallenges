def debug(f):
  for y in f:
    print("".join(map(str, y)))

def s2l(s):
  return list(map(int, list(s)))

def neigh(x, y):
  n = [ (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1) ]
  return list(filter(lambda p: p[0]>=0 and p[0]<10 and p[1]>=0 and p[1]<10, map(lambda f: (f[0] + x, f[1] + y), n)))

with open("input.txt", mode="r") as f:
  field = [ x.strip() for x in f.readlines() ]

#field = ["5483143223","2745854711","5264556173","6141336146","6357385478",
#"4167524645","2176841721","6882881134","4846848554","5283751526"]

field = list(map(lambda f: s2l(f), field))

step = 1
flashes = 0

while True:
  # first, increase all energy levels
  newfield = [ list(map(lambda n: n + 1, y)) for y in field ]

  # now let the flashing begin
  flashmap = [ [ 0 ] * 10 for y in range(10) ]

  while True:
    found = 0
    for y in range(10):
      for x in range(10):
        if newfield[y][x] > 9 and flashmap[y][x] == 0:
          # found a new flashing octopus
          flashmap[y][x] = 1
          newfield[y][x] = 0
          found = found + 1
          flashes = flashes + 1
          # increase all adjacent values
          for n in neigh(x, y):
            nx, ny = n
            if flashmap[ny][nx] == 0:
              newfield[ny][nx] = newfield[ny][nx] + 1
    if found == 0:
      break
#  print("After step {}".format(step))
#  print("field:")
#  debug(newfield)
#  print("flashes")
#  debug(flashmap)
#  print("")
  if step == 100:
    break;
  step = step + 1
  field = newfield

print(flashes)
