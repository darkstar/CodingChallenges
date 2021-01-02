import re

maskregex = re.compile(r"^mask = (?P<mask>[01X]{36})$")
memregex = re.compile(r"^mem\[(?P<addr>\d+)\] = (?P<val>\d+)$")

andmask = 1
ormask = 0

mem = {}

with open("input.txt", mode="r") as f:
    while True:
        l = f.readline().strip()

        if len(l) == 0:
            break

        m = maskregex.match(l)
        if m:
            rawmask = m.group("mask")
            andmask = "".join(map(lambda c: "0" if c == "0" else "1", rawmask))
            ormask = "".join(map(lambda c: "1" if c == "1" else "0", rawmask))
            andmask = int(andmask, 2)
            ormask = int(ormask, 2)
            continue

        m = memregex.match(l)
        if m:
            addr = int(m.group("addr"))
            val = int(m.group("val"))
            val = (val & andmask) | ormask
            mem[addr] = val
            continue

        print("invalid line: <{}>".format(l))
        exit(1)

s = 0
for k, v in mem.items():
    s += v

print(s)
