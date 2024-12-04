def is_safe(r):
    diffs = [ r[x + 1] - r[x] for x in range(len(r) - 1) ]
    ascending = all(map(lambda x: x > 0, diffs))
    descending = all(map(lambda x: x < 0, diffs))
    safe = (ascending or descending) and all(map(lambda x: abs(x) <= 3, diffs))
    return safe

def is_really_safe(r):
    dropped = [ r[:i] + r[i + 1:] for i in range(len(r)) ]
    return any(map(lambda x: is_safe(x), dropped))

with open("input.txt", mode="r") as f:
    reports = [ list(map(int, x.split())) for x in f.readlines() ]

print(len([x for x in reports if is_really_safe(x)]))
