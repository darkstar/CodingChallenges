ranges = []

with open("input.txt") as f:
    for l in f.readlines():
        vals = l.strip().split("-")
        ranges.append( { "a" : int(vals[0]), "b" : int(vals[1]) } )

ranges.sort(key = lambda x: x["a"])

ip = 0
for x in ranges:
    # skip the range if we're already past it
    if x["b"] < ip:
        continue
    # if the next range starts after the current IP, that IP is free
    if x["a"] > ip:
        break
    ip = x["b"] + 1

print(ip)
