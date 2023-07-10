#  1        +y
# 2+0    -x   +x
#  3        -y

dirs = { 0: (1, 0), 1: (0, 1), 2: (-1, 0), 3: (0, -1) }

state = { "x": 0, "y": 0, "wx": 10, "wy": 1, "d": 0 }

with open("input.txt", mode="r") as f:
    steps = [ (x[0], int(x[1:])) for x in f.readlines() ]

for s in steps:
    if s[0] == "N":
        state["wy"] += s[1]
    elif s[0] == "E":
        state["wx"] += s[1]
    elif s[0] == "S":
        state["wy"] -= s[1]
    elif s[0] == "W":
        state["wx"] -= s[1]
    elif s[0] == "F":
        state["x"] += s[1] * state["wx"] 
        state["y"] += s[1] * state["wy"]
    elif s[0] == "L":
        for a in range(s[1] // 90):
            tx, ty = state["wx"], state["wy"]
            state["wy"] = tx
            state["wx"] = -ty
    elif s[0] == "R":
        for a in range(s[1] // 90):
            tx, ty = state["wx"], state["wy"]
            state["wx"] = ty
            state["wy"] = -tx
    else:
        print("{} invalid".format(s[0]))
        exit(1)

print("{}".format(abs(state["x"]) + abs(state["y"])))
