import itertools

with open("input.txt") as f:
    lines = f.readlines()

total = 0

for l in lines:
    vals = list(map(int, l.strip().split()))
    perms = itertools.permutations(vals, 2)
    for pair in perms:
        if pair[0] % pair[1] == 0:
            total += pair[0] // pair[1]
            break;

print(total)
