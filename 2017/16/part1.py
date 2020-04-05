with open("input.txt") as f:
    moves = f.readline().split(",")

programs = list("abcdefghijklmnop")

for step in moves:
    if step[0] == "s":
        # Spin
        val = int(step[1:])
        programs = programs[-val:] + programs[:-val]
    elif step[0] == "x":
        # Exchange
        (i1, i2) = step[1:].split("/")
        tmp = programs[int(i1)]
        programs[int(i1)] = programs[int(i2)]
        programs[int(i2)] = tmp
    elif step[0] == "p":
        # Partner
        (p1, p2) = step[1:].split("/")
        i1 = programs.index(p1)
        i2 = programs.index(p2)

        tmp = programs[i1]
        programs[i1] = programs[i2]
        programs[i2] = tmp

print("".join(programs))
