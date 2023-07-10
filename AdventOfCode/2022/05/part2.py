import itertools

with open("input.txt", mode="r") as f:
    stack = [ l[:-1] for l in itertools.takewhile(lambda x: len(x) > 2, f) ]
    stack.reverse()
    moves = [ l.strip() for l in f.readlines() ]

stacks = { int(k): [] for k in stack[0].split() }
numstacks = len(stacks)
for l in stack[1:]:
    for x in range(numstacks):
        pos = 4 * x + 1
        if l[pos] != " ":
            stacks[x + 1].append(l[pos])

for m in moves:
    s = m.split()
    n, x, y = int(s[1]), int(s[3]), int(s[5])
    crates = stacks[x][-n:]
    stacks[x] = stacks[x][:-n]
    stacks[y] += crates

result = ""
for x in range(numstacks):
    result += stacks[x + 1].pop(-1)

print(result)
