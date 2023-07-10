with open("input.txt") as f:
    code = list(map(int, f.readlines()))

steps = 0
pos = 0
while pos >= 0 and pos < len(code):
    # get jump target
    target = code[pos]
    # change jump offset
    if target >= 3:
        code[pos] -= 1
    else:
        code[pos] += 1
    # next instruction
    pos = pos + target
    # inc number of steps
    steps += 1

print(steps)
