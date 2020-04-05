import re

registers = {}

regex = re.compile(r'(\S+)\s* (inc|dec) (-?\d+) if (\S+) (>|<|>=|<=|==|!=) (-?\d+)')

maxval = 0

with open("input.txt") as f:
    lines = f.readlines()

for line in lines:
    m = regex.match(line)
    # split out all we need
    reg = m.group(1)
    op = m.group(2)
    val = int(m.group(3))
    pred = m.group(4)
    comp = m.group(5)
    predval = int(m.group(6))
    # ensure register exists
    if not reg in registers:
        registers[reg] = 0
    if not pred in registers:
        registers[pred] = 0
    # check predicate
    if comp == ">": 
        result = registers[pred] > predval
    elif comp == "<": 
        result = registers[pred] < predval
    elif comp == ">=": 
        result = registers[pred] >= predval
    elif comp == "<=":
        result = registers[pred] <= predval
    elif comp == "==":
        result = registers[pred] == predval
    elif comp == "!=":
        result = registers[pred] != predval

    if result:
        oldval = registers[reg]
        if op == "inc":
            registers[reg] += val
        else:
            registers[reg] -= val
        if registers[reg] > maxval:
            maxval = registers[reg]

print(maxval)
