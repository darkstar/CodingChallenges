garbage = 0

with open("input.txt") as f:
    stream = f.readline().strip()

pos = 0
while pos < len(stream):
    ch = stream[pos]
    if ch == "<":
        # garbage. skip
        pos += 1
        while True:
            x = stream[pos]
            if x == "!":
                pos += 2
                continue
            if x == ">":
                break
            garbage += 1
            pos += 1

    pos += 1

print(garbage)

