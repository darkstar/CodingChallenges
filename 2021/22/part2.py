import re

# this is so ugly it's embarrassing ;-)

def intersect(a1,a2,b1,b2):
  v = max(a1,b1)
  w = min(a2,b2)
  if v <= w:
    return (v, w)
  return None

def intersect3(x1,x2,y1,y2,z1,z2,x3,x4,y3,y4,z3,z4):
  u = intersect(x1,x2,x3,x4)
  v = intersect(y1,y2,y3,y4)
  w = intersect(z1,z2,z3,z4)
  if u and v and w:
    return u[0],u[1],v[0],v[1],w[0],w[1]
  return None

def vol(x1,x2,y1,y2,z1,z2):
  u = abs(x1-x2)+1
  v = abs(y1-y2)+1
  w = abs(z1-z2)+1
  return u*v*w

r = re.compile(r"(on|off) x=([-0-9]+)..([-0-9]+),y=([-0-9]+)..([-0-9]+),z=([-0-9]+)..([-0-9]+)")

with open("input.txt", mode="r") as f:
  a = f.readlines()

l = list(map(lambda m: (m.group(1)=="on", *[int(m.group(k)) for k in range(2, 8)]), [ r.match(x) for x in a ]))

on = []
off = []
oncount = 0

for c in l:
  newon = []
  newoff = []
  if c[0]:
    # turn ON
    newon.append((c[1],c[2],c[3],c[4],c[5],c[6]))
    oncount += vol(c[1],c[2],c[3],c[4],c[5],c[6])
  for oc in on:
    i = intersect3(c[1],c[2],c[3],c[4],c[5],c[6], oc[0],oc[1],oc[2],oc[3],oc[4],oc[5])
    if i:
      oncount -= vol(i[0],i[1],i[2],i[3],i[4],i[5])
      newoff.append(i)
  for oc in off:
    i = intersect3(c[1],c[2],c[3],c[4],c[5],c[6], oc[0],oc[1],oc[2],oc[3],oc[4],oc[5])
    if i:
      oncount += vol(i[0],i[1],i[2],i[3],i[4],i[5])
      newon.append(i)
  on = on + newon
  off = off + newoff

print(oncount)
