import re

maskregex = re.compile(r"^mask = (?P<mask>[01X]{36})$")
memregex = re.compile(r"^mem\[(?P<addr>\d+)\] = (?P<val>\d+)$")

ormask = 0

mem = {}

def dofloat(x, l):
    if len(l) == 0:
        return [ x ]
    a = l[0]
    b = l[1:]
    omask = 1 << a
    amask = ~(1 << a)
    return dofloat(x & amask, b) + dofloat(x | omask, b) 

with open("input.txt", mode="r") as f:
    while True:
        l = f.readline().strip()

        if len(l) == 0:
            break

        m = maskregex.match(l)
        if m:
            rawmask = m.group("mask")
            ormask = "".join(map(lambda c: "1" if c == "1" else "0", rawmask))
            ormask = int(ormask, 2)
            floatidx = [ 35 - i for i, x in enumerate(rawmask) if x == "X" ]
            continue

        m = memregex.match(l)
        if m:
            addr = int(m.group("addr")) | ormask
            val = int(m.group("val"))
            alladdrs = dofloat(addr, floatidx)
            for addr in alladdrs:
                mem[addr] = val
            continue

        print("invalid line: <{}>".format(l))
        exit(1)

s = 0
for k, v in mem.items():
    s += v

print(s)
