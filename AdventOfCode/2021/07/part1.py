with open("input.txt", mode="r") as f:
  xcrabs = [ int(i) for i in f.readline().split(",") ]

crabs = {}

for x in xcrabs:
  if x in crabs:
    crabs[x] = crabs[x] + 1
  else:
    crabs[x] = 1

mincrab = min(crabs)
maxcrab = max(crabs)
minfuel = 999999999

for pos in range(mincrab, maxcrab + 1):
  fuel = 0
  for c in crabs:
    delta = abs(c - pos)
    fuel += delta * crabs[c]
  if fuel < minfuel:
    minfuel = fuel

print(minfuel)
