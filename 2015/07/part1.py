import re

resolved = {}

def getval(s):
    global resolved

    if s.isnumeric():
        return int(s)
    if s in resolved:
        return resolved[s]

    return None

with open('input.txt', mode='r') as f:
    cmds = f.readlines()

    while 'a' not in resolved:
        for cmd in cmds:
            m = re.match('(.*) -> (.*)', cmd)
            dest_wire = m.groups()[1]
            src = m.groups()[0]

            # skip all signals we already have
            if getval(dest_wire) is not None:
                continue

            # check if it's just a number
            if src.isnumeric():
                resolved[dest_wire] = int(src)
                continue

            parts = src.split()

            # check for simple copy
            if len(parts) == 1 and parts[0] in resolved:
                resolved[dest_wire] = resolved[parts[0]]
                continue

            # check for NOT
            if len(parts) == 2 and parts[0] == 'NOT' and getval(parts[1]) is not None:
                resolved[dest_wire] = (~getval(parts[1])) & 0xffff
                continue

            # check for RSHIFT and LSHIFT
            if len(parts) == 3 and parts[1].endswith('SHIFT') and getval(parts[0]) is not None and parts[2].isnumeric():
                if parts[1][0] == 'R':
                    resolved[dest_wire] = (getval(parts[0]) >> int(parts[2])) & 0xffff
                else:
                    resolved[dest_wire] = (getval(parts[0]) << int(parts[2])) & 0xffff
                continue

            if len(parts) == 3 and parts[1] == 'AND' and getval(parts[0]) is not None and getval(parts[2]) is not None:
                resolved[dest_wire] = getval(parts[0]) & getval(parts[2])
                continue

            if len(parts) == 3 and parts[1] == 'OR' and getval(parts[0]) is not None and getval(parts[2]) is not None:
                resolved[dest_wire] = getval(parts[0]) | getval(parts[2])
                continue

print(resolved['a'])

