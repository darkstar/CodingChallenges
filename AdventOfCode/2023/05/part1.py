def domap(val, rules):
    for r in rules:
        if val >= r[1] and val < r[1] + r[2]:
            return val - r[1] + r[0]
    return val

maps = []

with open("input.txt", mode="r") as f:
    seeds = list(map(int, f.readline().strip().split(":")[1].split()))
    f.readline()
    mapname = ""
    rules = []
    for l in f:
        l = l.strip()
        if "map" in l:
            mapname = l.split(":")[0].strip()
            rules = []
        elif len(l) > 0:
            rules.append(list(map(int, l.split())))
        else:
            maps.append( (mapname, rules) )
    maps.append( (mapname, rules) )

for m in maps:
    seeds = list(map(lambda v: domap(v, m[1]), seeds))

print(min(seeds))
