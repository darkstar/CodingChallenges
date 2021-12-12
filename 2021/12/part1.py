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
  path = paths.pop()
  # finished?
  if path[-1] == "end":
    complete.append(path)
    continue
  # find possible routes
  for rt in adj[path[-1]]:
    # skip if small and already visited
    if rt.islower() and rt in path:
      continue
    # else append next step and continue
    newpath = path.copy()
    newpath.append(rt)
    paths.append(newpath)

print(len(complete))
