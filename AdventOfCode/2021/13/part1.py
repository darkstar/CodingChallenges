dots = []

with open("input.txt", mode="r") as f:
  while True:
    l = f.readline().strip()
    if l == "":
      break;
    x, y = l.split(",")
    dots.append((int(x), int(y)))

  folds = [ x.strip() for x in f.readlines() ]

# debug
#dots = [(6,10),(0,14),(9,10),(0,3),(10,4),(4,11),(6,0),(6,12),(4,1),(0,13),(10,12),
#(3,4),(3,0),(8,4),(1,10),(2,14),(8,10),(9,0)]
#folds = ["fold along y=7",  "fold along x=5" ]

folds = list(map(lambda p: (p[0][-1], int(p[1])), [ x.split("=") for x in folds ]))

f = folds[0]

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

print(len(odots))
