import re

nodes = {}

with open("input.txt") as f:
    nodemap = f.readlines()

for n in nodemap:
    m = re.match(r'(\d+) <-> ([\d ,]+)', n)
    nodes[m.group(1)] = { "id": m.group(1), "neighbors": m.group(2).split(", ") }

# walk from node 0
seen = set()
queue = [ nodes["0"] ]

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

print(len(seen))
