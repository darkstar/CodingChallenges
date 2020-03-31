import re

with open("input.txt") as f:
    df = f.readlines()[2:]

noderegex = re.compile(r'/dev/grid/node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T\s+(\d+)%')

nodes = {}
dimension = (0, 0)

for line in df:
    m = noderegex.match(line)
    if m:
        x = int(m.group(1))
        y = int(m.group(2))
        nodes[ (x, y) ] = { "x": x, "y": y, "size": int(m.group(3)), 
            "used": int(m.group(4)), "avail": int(m.group(5)), "pct": int(m.group(6)) }
        if x > dimension[0]:
            dimension = (x, dimension[1])
        if y > dimension[1]:
            dimension = (dimension[0], y)
        pass
    else:
        print("Invalid line: {}".format(line))
        exit(1)

viable = []

for src in nodes.values():
    for dst in nodes.values():
        # skip if nodes are the same
        if src == dst:
            continue
        # skip if node a is empty
        if src["used"] == 0:
            continue
        # test if data on node A fits on node B
        if src["used"] < dst["avail"]:
            viable.append( (src, dst) )

print(len(viable))
