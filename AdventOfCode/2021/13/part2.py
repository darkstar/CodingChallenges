from functools import reduce

dots = []

with open("input.txt", mode="r") as f:
  while True:
    l = f.readline().strip()
    if l == "":
      break;
    x, y = l.split(",")
    dots.append((int(x), int(y)))

  folds = [ x.strip() for x in f.readlines() ]

folds = list(map(lambda p: (p[0][-1], int(p[1])), [ x.split("=") for x in folds ]))

for f in folds:
  if f[0] == "x":
    odots = list(filter(lambda p: p[0] < f[1], dots)) # original dots
    fdots = list(filter(lambda p: p[0] > f[1], dots)) # dots to fold
    refl = list(map(lambda p: (2 * f[1] - p[0], p[1]), fdots)) # reflected positions
  else:
    odots = list(filter(lambda p: p[1] < f[1], dots)) # original dots
    fdots = list(filter(lambda p: p[1] > f[1], dots)) # dots to fold
    refl = list(map(lambda p: (p[0], 2 * f[1] - p[1]), fdots)) # reflected positions
  
  for p in refl:
    if not p in odots:
      odots.append(p)
  dots = odots

bbox = reduce(lambda b, x: (max(b[0], x[0]), max(b[1], x[1])), dots, (0, 0))
for y in range(bbox[1] + 1):
  for x in range(bbox[0] + 1):
    c = '#' if (x, y) in dots else ' '
    print(c, end='')
  print("")
