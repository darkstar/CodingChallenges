import functools
import operator

with open("input.txt") as f:
    steps = list(map(ord, f.readline().strip()))

lst = [ x for x in range(256) ]
pos = 0
skipsize = 0

# salt the input
steps += [17, 31, 73, 47, 23]

# calculate 64 rounds for the sparse hash
for rnd in range(64):
    for s in steps:
        # start swapping from p1 to p2
        p1 = pos
        p2 = pos + s - 1
        while p2 > p1:
            # swap p1 and p2, and move them
            tmp = lst[p1 % len(lst)]
            lst[p1 % len(lst)] = lst[p2 % len(lst)]
            lst[p2 % len(lst)] = tmp
            p1 += 1
            p2 -= 1
        pos = (pos + s + skipsize) % len(lst)
        skipsize += 1

densehash = []

# reduce to dense hash
for block in range(16):
    sublst = lst[block * 16:(block + 1)*16]
    densehash.append("{0:02x}".format(functools.reduce(operator.xor, sublst)))

print("".join(densehash))
