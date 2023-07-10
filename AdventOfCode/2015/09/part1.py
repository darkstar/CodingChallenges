class Node:
    def __init__(self, name):
        self.name = name
        self.dists = {}

all_nodes = {}
minimum = 999999999

def visit(n, remaining, dist):
    global minimum

    for next_hop in remaining:
        visit(next_hop, [x for x in remaining if x.name != next_hop.name], dist + n.dists[next_hop])
    if len(remaining) == 0:
        if dist < minimum:
            minimum = dist

with open('input.txt', mode='r') as f:
    for line in f.readlines():
        words = line.split()
        if words[0] not in all_nodes:
            all_nodes[words[0]] = Node(words[0])
        if words[2] not in all_nodes:
            all_nodes[words[2]] = Node(words[2])
        from_node = all_nodes[words[0]]
        to_node = all_nodes[words[2]]
        distance = int(words[4])
        from_node.dists[to_node] = distance
        to_node.dists[from_node] = distance

    for start_node in all_nodes:
        visit(all_nodes[start_node], [x[1] for x in all_nodes.items() if x[0] != start_node], 0)

print(minimum)

