validtriangles = 0

def isvalid(a, b, c):
    return (a + b > c) and (a + c > b) and (b + c > a)

def checktri(x, y, z):
    global validtriangles

    if isvalid(int(x), int(y), int(z)):
        validtriangles += 1

with open("input.txt", mode="r") as f:
    triangles = f.readlines()

    while len(triangles) > 0:
        r1 = triangles.pop(0).split()
        r2 = triangles.pop(0).split()
        r3 = triangles.pop(0).split()

        checktri(r1[0], r2[0], r3[0])
        checktri(r1[1], r2[1], r3[1])
        checktri(r1[2], r2[2], r3[2])

print(validtriangles)
