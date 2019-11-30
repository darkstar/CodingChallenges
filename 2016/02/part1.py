
def nextpos(pos, button):
    (x, y) = pos
    if button == "U": y = max(0, y - 1)
    if button == "D": y = min(2, y + 1)
    if button == "L": x = max(0, x - 1)
    if button == "R": x = min(2, x + 1)
    return (x, y)

def keyatpos(pos):
    lookup = { (0, 0): 1, (1, 0): 2, (2, 0): 3,
               (0, 1): 4, (1, 1): 5, (2, 1): 6,
               (0, 2): 7, (1, 2): 8, (2, 2): 9 }
    return lookup[pos]

with open("input.txt", mode="r") as f:
    instructions = f.readlines()

    for step in instructions:
        pos = (1, 1)
        for ch in step.strip():
            pos = nextpos(pos, ch)
        print(keyatpos(pos), end="")

print()
