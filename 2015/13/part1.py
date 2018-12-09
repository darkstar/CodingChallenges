import itertools

names = []
deltas = {}
max_happiness = 0

def evaluate(p):
    happiness = 0

    for i in range(len(p)):
        left = (i - 1) % len(p)
        right = (i + 1) % len(p)
        left_weight = deltas[p[i]][p[left]]
        right_weight = deltas[p[i]][p[right]]
        happiness += left_weight + right_weight

    return happiness

with open('input.txt', mode='r') as f:
    lines = [x.rstrip()[:-1] for x in f.readlines()]
    for x in lines:
       w = x.split()
       name, value, neighbor = w[0], int(w[3]) if w[2] == "gain" else -int(w[3]), w[10]

       if name not in names:
           names.append(name)
           deltas[name] = {}

       deltas[name][neighbor] = value

for p in itertools.permutations(names):
    happiness = evaluate(p)
    if happiness > max_happiness:
        max_happiness = happiness

print(max_happiness)
