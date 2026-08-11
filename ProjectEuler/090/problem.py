import itertools

def fixup(cube):
    c = set(cube)
    if 6 in c or 9 in c:
        c.add(6)
        c.add(9)
    return c

squares = [ (0, 1), (0, 4), (0, 9), (1, 6), (2, 5), (3, 6), (4, 9), (6, 4), (8, 1) ]

def valid(c1, c2):
    for (a, b) in squares:
        if not ((a in c1 and b in c2) or (a in c2 and b in c1)):
            return False
    return True

cubes = [ fixup(x) for x in itertools.combinations(range(10), 6)]

result = 0

for i in range(len(cubes)):
    for j in range(i, len(cubes)):
        c1 = cubes[i]
        c2 = cubes[j]

        if valid(c1, c2):
            result += 1

print(result)
