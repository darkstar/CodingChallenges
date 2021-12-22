import re

r = re.compile(r"(on|off) x=([-0-9]+)..([-0-9]+),y=([-0-9]+)..([-0-9]+),z=([-0-9]+)..([-0-9]+)")

with open("input.txt", mode="r") as f:
  l = list(map(lambda m: (m.group(1)=="on", *[int(m.group(k)) for k in range(2, 8)]), [ r.match(x) for x in f.readlines() ]))

# only cubes with coordinates in -50..50
l = list(filter(lambda m: all([ -50 <= m[v] <= 50 for v in range(1,7)]), l))

cubes = {}
for c in l:
  for x in range(c[1], c[2]+1):
    for y in range(c[3], c[4]+1):
      for z in range(c[5], c[6]+1):
        if c[0]:
          # turn ON
          cubes[(x,y,z)] = 1
        else:
          # turn OFF
          if (x,y,z) in cubes:
            del cubes[(x,y,z)]
          
print(len(cubes))
