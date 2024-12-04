with open("input.txt") as f:
    l = [ x.strip().split("  ") for x in f.readlines()]
    l = [ (int(x[0]), int(x[1])) for x in l ]
    l = list(map(list, zip(*l)))

left = sorted(l[0])
right = sorted(l[1])

s = sum(map(lambda a, b: abs(b - a), left,right))

print(s)