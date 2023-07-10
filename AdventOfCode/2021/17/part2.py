import re

# assumes the target area is below x-axis
def simulate(xv, yv, target):
  maxy = 0
  x = 0
  y = 0
  while True:
    x = x + xv
    y = y + yv
    # check new peak
    if y > maxy:
      maxy = y
    # change velocities
    if xv > 0:
      xv -= 1
    yv -= 1
    # check out of bounds
    if x > target[1]:
      return False, 0
    if y < target[2]:
      return False, 0
    # check target
    if x >= target[0] and x <= target[1] and y <= target[3] and y >= target[2]:
      return True, maxy

with open("input.txt", mode="r") as f:
  l = f.readline()
#  l = "target area: x=20..30, y=-10..-5"
  m = re.search('x=([-\d]+)..([-\d]+), y=([-\d]+)..([-\d]+)', l)
  target = list(map(int, m.groups()))

# determine minimum required x velocity to even rech target area
# assumes target area is to the right (x positive)
xpos = 0
minxvel = 0
while xpos < target[0]:
  minxvel += 1
  xpos += minxvel

maxxvel = target[1]
minyvel = -200 
maxyvel = 200 # kinda arbitrary

vals = []

for xv in range(minxvel, maxxvel + 1):
  for yv in range(minyvel, maxyvel + 1):
    hit, peak = simulate(xv, yv, target)
    if hit:
      vals.append((xv, yv))

print(len(vals))

