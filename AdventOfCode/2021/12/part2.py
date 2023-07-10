def gettwice(p):
  c = {}
  for x in p:
    # only count small caves
    if not x.islower():
      continue
    if not x in c:
      c[x] = 0
    c[x] = c[x] + 1
  dbl = [ x for x in c if c[x] == 2 ]
  if len(dbl) == 0:
    return None
  return dbl[0]

def count(p, x):
  return len([k for k in p if k == x])

def canenter(p, n):
  # we can enter the cave if it's a big cave
  if n.isupper():
    return True
  # we can also enter a small when we haven't bene there yet
  numvisit = count(p,n)
  if numvisit == 0:
    return True
  # if we were in this cave already twice, we cannot enter again
  if numvisit == 2:
    return False
  # see which cave we visited twice
  twice = gettwice(p)
  # we can enter if we have not visited any cave twice
  if not twice:
    return True
  # we visited another cave twice, so we cannot visit this one twice
  return False

with open("input.txt", mode="r") as f:
  m = [ x.strip() for x in f.readlines() ]

#m = [ "start-A", "start-b", "A-c", "A-b", "b-d", "A-end", "b-end" ]

adj = {}

# build adjacency matrix
for l in m:
  a, b = l.split("-")
  if not a in adj:
    adj[a] = []
  if not b in adj:
    adj[b] = []

  adj[a].append(b)
  adj[b].append(a)

paths = [ [ "start" ] ]
complete = []

while len(paths)>0:
  # take the next path
  path = paths.pop(0)
  # finished?
  if path[-1] == "end":
    complete.append(path)
    continue
  # find possible routes
  for rt in adj[path[-1]]:
    # canot return to start
    if rt == "start":
      continue
    if rt.islower():
      if not canenter(path, rt):
        continue

    # else append next step and continue
    newpath = path.copy()
    newpath.append(rt)
    paths.append(newpath)

print(len(complete))

