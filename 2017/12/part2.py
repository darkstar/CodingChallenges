import re

nodes = {}

def connected(nodes, n):
    # walk from node n
    seen = set()
    queue = [ nodes[n] ]

    while True:
        # finish of we have no further nodes to check
        if len(queue) == 0:
            break
        # get the next node
        nextnode = queue.pop(0)
        # remember that we've visited it
        seen.add(nextnode["id"])
        for n in nextnode["neighbors"]:
            if not n in seen:
                queue.append(nodes[n])
    return list(seen)

def firstnotinlist(l, total):
    x = 0
    while x < total:
        if x not in l:
            return x
        x += 1
    return -1

with open("input.txt") as f:
    nodemap = f.readlines()

for n in nodemap:
    m = re.match(r'(\d+) <-> ([\d ,]+)', n)
    nodes[int(m.group(1))] = { "id": int(m.group(1)), "neighbors": list(map(int, m.group(2).split(", "))) }

totalseen = []
groups = 0

while len(totalseen) < len(nodes):
    # find first node we have not visited yet
    n = firstnotinlist(totalseen, len(nodes))
    grp = connected(nodes, n)
    groups += 1
    totalseen += grp

print(groups)
