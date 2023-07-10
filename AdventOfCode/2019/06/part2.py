orbits = { }

def orbitpath(b):
    res = []
    while b != "COM":
        b = orbits[b]
        res.append(b)

    return res

def commonpath(p1, p2):
    while p1[len(p1)-1] == p2[len(p2)-1]:
        p1.pop()
        p2.pop()
    return (p1, p2)

with open("input.txt", mode="r") as f:
    for l in f.readlines():
        data = l.strip().split(")")
        orbits[data[1]] = data[0]

path1 = orbitpath("YOU")
path2 = orbitpath("SAN")
cpath = commonpath(path1, path2)

print(len(cpath[0]) + len(cpath[1]))

