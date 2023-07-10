import itertools

containers = []
solutions = {}

def measure(x):
    return sum([containers[i] for i in range(len(containers)) if x[i] == 1])

with open('input.txt', mode='r') as f:
    lines = f.readlines()
    for c in lines:
        containers.append(int(c.rstrip()))

for selection in itertools.product([0, 1], repeat = len(containers)):
    if measure(selection) == 150:
        bits = len([x for x in selection if x == 1])
        if not bits in solutions: solutions[bits] = 0
        solutions[bits] += 1

print(solutions[min(solutions)])
