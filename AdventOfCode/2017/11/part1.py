with open("input.txt") as f:
    steps = f.readline().strip().split(",")

# using cube coordinates
# see https://www.redblobgames.com/grids/hexagons/

pos = (0, 0, 0)
delta = { "n": (0, 1, -1), "s": (0, -1, 1), 
          "ne": (1, 0, -1), "sw": (-1, 0, 1), 
          "se": (1, -1, 0), "nw": (-1, 1, 0) }

for s in steps:
    d = delta[s]
    pos = (pos[0] + d[0], pos[1] + d[1], pos[2] + d[2])

dist = (abs(pos[0]) + abs(pos[1]) + abs(pos[2])) // 2

print(dist)
