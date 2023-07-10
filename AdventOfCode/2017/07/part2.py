import re

def weight(n):
    node = nodes[n]
    w = node["weight"]
    if node["children"]:
        for x in node["children"]:
            w += weight(x)
    return w

def depth(n):
    if not nodes[n]["parent"]:
        return 0
    return 1 + depth(nodes[n]["parent"])

with open("input.txt") as f:
    lines = f.readlines()

nodes = {}

for line in lines:
    m = re.match(r'([^\s]+)\s\((\d+)\)(\s*->\s)?(.*)?$', line)
    if m:
        node = { "name": m.group(1), 
                 "weight": int(m.group(2)), 
                 "children": None if not m.group(4) else m.group(4).split(", "),
                 "chweights": [],
                 "depth": 0,
                 "parent": None }
        nodes[m.group(1)] = node

# find parents
for n in nodes:
    children = nodes[n]["children"]
    if children:
        for c in children:
            nodes[c]["parent"] = n

# fill child weights and distance to root
for n in nodes:
    nodes[n]["depth"] = depth(n)
    if nodes[n]["children"]:
        for ch in nodes[n]["children"]:
            nodes[n]["chweights"].append(weight(ch))

# find node without parents
rootnode = list(filter(lambda x: not nodes[x]["parent"], nodes))[0]

# find nodes with not all child weights the same
unbalanced = list(filter(lambda x: nodes[x]["children"] and len(set(nodes[x]["chweights"])) > 1, nodes))
unbalanced.sort(key = lambda x: -nodes[x]["depth"])
victim = unbalanced[0]

# move the culprit to the front of the list
culprits = list(zip(nodes[victim]["children"], nodes[victim]["chweights"]))
culprits.sort(key = lambda x: x[1])
if culprits[0][1] == culprits[1][1]:
    culprits.reverse()

culprit = culprits[0][0]

# calculate weight difference needed
wrongweight = culprits[0][1]
correctweight = culprits[1][1]

delta = correctweight - wrongweight

# fixup weight
nodes[culprit]["weight"] += delta
print(nodes[culprit]["weight"])
