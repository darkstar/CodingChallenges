#  1        +y
# 2+0    -x   +x
#  3        -y

dirs = { 0: (1, 0), 1: (0, 1), 2: (-1, 0), 3: (0, -1) }

state = { "x": 0, "y": 0, "d": 0 }

with open("input.txt", mode="r") as f:
    steps = [ (x[0], int(x[1:])) for x in f.readlines() ]

for s in steps:
    if s[0] == "N":
        state["y"] += s[1]
    elif s[0] == "E":
        state["x"] += s[1]
    elif s[0] == "S":
        state["y"] -= s[1]
    elif s[0] == "W":
        state["x"] -= s[1]
    elif s[0] == "F":
        state["x"] += s[1] * dirs[state["d"]][0]
        state["y"] += s[1] * dirs[state["d"]][1]
    elif s[0] == "L":
        state["d"] = (state["d"] + s[1] // 90) % 4
    elif s[0] == "R":
        state["d"] = (state["d"] - s[1] // 90) % 4
    else:
        print("{} invalid".format(s[0]))
        exit(1)

print("{}".format(abs(state["x"]) + abs(state["y"])))
