import collections

with open("input.txt", mode="r") as f:
    jolts = [ int(x.strip()) for x in f.readlines() ]

jolts.sort()

j1 = [0] + jolts.copy()
j2 = jolts.copy() + [jolts[-1] + 3]

diffs = list(map(lambda x: x[1] - x[0], zip(j1, j2)))

cdict = dict(collections.Counter(diffs))

print(cdict[1] * cdict[3])
