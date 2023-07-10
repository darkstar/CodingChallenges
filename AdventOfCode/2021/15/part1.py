from functools import reduce

XSIZE=10
YSIZE=10

def minneigh(p, f):
  n = [ (0, -1), (-1, 0), (1, 0), (0, 1) ]
  np = list(filter(lambda k: k[0]>=0 and k[0] < XSIZE and k[1]>=0 and k[1] < YSIZE, map(lambda x: (p[0]+x[0], p[1]+x[1]), n)))
  vals = list(map(lambda p: f[p[1]][p[0]], np))
  if len(vals) == 0:
    return 0
  return min(vals)

with open("input.txt", mode="r") as f:
  risks = [ x.strip() for x in f.readlines() ]

#risks = [ "1163751742", "1381373672", "2136511328", "3694931569", "7463417111",
#"1319128137", "1359912421", "3125421639", "1293138521", "2311944581"]

risks = [ list(map(int, list(p))) for p in risks ]

YSIZE = len(risks)
XSIZE = len(risks[0])

risks[0][0] = 0
pmap = [ [ 99999 ] * XSIZE for x in range(YSIZE) ]
pmap[YSIZE-1][XSIZE-1] = risks[YSIZE-1][XSIZE-1]

while True:
#for step in range(10):
  changed = 0
  for y in range(YSIZE):
    for x in range(XSIZE):
      v = risks[y][x]
      mr = minneigh((x,y), pmap)
      if mr != 0 and mr+v < pmap[y][x]:
        pmap[y][x] = mr + v
        changed = changed + 1
  if changed == 0:
    break

print(pmap[0][0])
