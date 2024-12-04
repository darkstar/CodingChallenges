with open("input.txt") as f:
    l = [ x.strip().split("  ") for x in f.readlines()]
    l = [ (int(x[0]), int(x[1])) for x in l ]
    l = list(map(list, zip(*l)))

score = 0
for x in l[0]:
    n = l[1].count(x)
    score += x * n

print(score)