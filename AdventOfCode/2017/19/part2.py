def step(p, d):
    if d == "u":
        return (p[0], p[1] - 1)
    if d == "d":
        return (p[0], p[1] + 1)
    if d == "l":
        return (p[0] - 1, p[1])
    if d == "r":
        return (p[0] + 1, p[1])

with open("input.txt") as f:
    maze = f.readlines()

pos = (maze[0].index("|"), 0)
direction = "d"

letters = []
steps = 0
while True:
    # move a step
    pos = step(pos, direction)
    steps += 1
    # check position
    ch = maze[pos[1]][pos[0]]
    if ch == " ":
        # end of the line
        break
    if ch == "+":
        if direction in ['u','d']:
            direction = "l" if maze[pos[1]][pos[0] - 1] == "-" else "r"
        elif direction in ['l', 'r']:
            direction = "u" if maze[pos[1] - 1][pos[0]] == "|" else "d"
    if ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        letters.append(ch)

print(steps)
