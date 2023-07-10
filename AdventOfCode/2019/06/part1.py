orbits = { }

def orbitpath(b):
    res = []
    while b != "COM":
        b = orbits[b]
        res.append(b)

    return res

with open("input.txt", mode="r") as f:
    for l in f.readlines():
        data = l.strip().split(")")
        orbits[data[1]] = data[0]

totalorbits = 0

for k in orbits:
    totalorbits += len(orbitpath(k))

print(totalorbits)
