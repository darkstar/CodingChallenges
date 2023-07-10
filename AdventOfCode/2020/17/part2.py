space = {}
xr = (0, 0)
yr = (0, 0)
zr = (0, 0)
wr = (0, 0)

def sset(x, y, z, w, act, space):
  global xr, yr, zr, wr
  p = (x, y, z, w)

  # update dict
  if not act:
    if p in space:
      del space[p]
  else:
    space[p] = '#'
    # update bbox
    xr = (min(xr[0], x), max(xr[1], x))
    yr = (min(yr[0], y), max(yr[1], y))
    zr = (min(zr[0], z), max(zr[1], z))
    wr = (min(wr[0], w), max(wr[1], w))

def sget(x, y, z, w, space):
  p = (x, y, z, w)
  if p in space:
    return "#"
  else:
    return "."

def neigh(x, y, z, w, space):
  r = 0
  for zz in range(z - 1, z + 2):
    for yy in range(y - 1, y + 2):
      for xx in range(x - 1, x + 2):
        for ww in range(w - 1, w + 2):
          if sget(xx, yy, zz, ww, space) == "#" and (xx, yy, zz, ww) != (x, y, z, w):
            r += 1
  return r

def evolveone(x, y, z, w, space, spacenew):
  n = neigh(x, y, z, w, space)
  if sget(x, y, z, w, space) == "#":
    if n < 2 or n > 3:
      sset(x, y, z, w, False, spacenew)
    else:
      sset(x, y, z, w, True, spacenew)
  else:
    if n == 3:
      sset(x, y, z, w, True, spacenew)
    else:
      sset(x, y, z, w, False, spacenew)

def evolve(space):
  global xr, yr, zr, wr
  spacenew = {}
  xxr = range(xr[0] - 1, xr[1] + 2)
  yyr = range(yr[0] - 1, yr[1] + 2)
  zzr = range(zr[0] - 1, zr[1] + 2)
  wwr = range(wr[0] - 1, wr[1] + 2)
  for w in wwr:
    for z in zzr:
      for y in yyr:
        for x in xxr:
          evolveone(x, y, z, w, space, spacenew)
  return spacenew
        
def printlayer(z, w, space):
  global xr, yr
  print("z={} w={}:".format(z, w))
  for y in range(yr[0], yr[1]+1):
    for x in range(xr[0], xr[1]+1):
      print("{}".format(sget(x, y, z, w, space)), end='')
    print("")
  print("")

def printall(space):
  global zr, wr
  for w in range(wr[0], wr[1]+1):
    for z in range(zr[0], zr[1]+1):
      printlayer(z, w, space)

# base setup
#sset(-1, 1, 0, 0, True, space)
#sset(0, -1, 0, 0, True, space)
#sset(0, 1, 0, 0, True, space)
#sset(1, 0, 0, 0, True, space)
#sset(1, 1, 0, 0, True, space)

with open("input.txt", mode="r") as f:
  lines = f.readlines()

for y in range(len(lines)):
  line = lines[y].strip()
  for x in range(len(line)):
    sset(x, y, 0, 0, line[x] == "#", space)

for x in range(6):
  space = evolve(space)

print(len(space))
