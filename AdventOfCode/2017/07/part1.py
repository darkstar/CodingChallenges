import re

with open("input.txt") as f:
    lines = f.readlines()

nodes = {}

for line in lines:
    m = re.match(r'([^\s]+)\s\((\d+)\)(\s*->\s)?(.*)?$', line)
    if m:
        node = { "name": m.group(1), 
                 "size": int(m.group(2)), 
                 "children": None if not m.group(4) else m.group(4).split(", "),
                 "parent": None }
        nodes[m.group(1)] = node

# find parents
for n in nodes:
    children = nodes[n]["children"]
    if children:
        for c in children:
            nodes[c]["parent"] = n

# find nodes without parents
roots = list(filter(lambda x: not nodes[x]["parent"], nodes))

print(roots[0])
