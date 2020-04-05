weight = 0
total = 0

with open("input.txt") as f:
    stream = f.readline().strip()

pos = 0
while pos < len(stream):
    ch = stream[pos]
    if ch == "{":
        # new group
        weight += 1
        total += weight
    elif ch == "}":
        # close group
        weight -= 1
    elif ch == "<":
        # garbage. skip
        pos += 1
        while True:
            x = stream[pos]
            if x == "!":
                pos += 2
                continue
            if x == ">":
                break
            pos += 1

    pos += 1

print(total)

