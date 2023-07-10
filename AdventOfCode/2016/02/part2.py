lookup = {                           (2, 0): '1',
                        (1, 1): '2', (2, 1): '3', (3, 1): '4',
           (0, 2): '5', (1, 2): '6', (2, 2): '7', (3, 2): '8', (4, 2): '9',
                        (1, 3): 'A', (2, 3): 'B', (3, 3): 'C',
                                     (2, 4): 'D'}

def nextpos(pos, button):
    global lookup

    (x, y) = pos
    if button == "U": y = y - 1
    if button == "D": y = y + 1
    if button == "L": x = x - 1
    if button == "R": x = x + 1
    # only allow legal moves...
    if (x, y) in lookup:
        return (x, y)
    # otherwise return previous position
    return pos

def keyatpos(pos):
    global lookup

    return lookup[pos]

with open("input.txt", mode="r") as f:
    instructions = f.readlines()

    for step in instructions:
        pos = (0, 2)
        for ch in step.strip():
            pos = nextpos(pos, ch)
        print(keyatpos(pos), end="")

print()
