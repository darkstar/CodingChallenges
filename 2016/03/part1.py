validtriangles = 0

def isvalid(a, b, c):
    return (a + b > c) and (a + c > b) and (b + c > a)

with open("input.txt", mode="r") as f:
    triangles = f.readlines()

    for tri in triangles:
        lengths = tri.strip().split()

        if isvalid(int(lengths[0]), int(lengths[1]), int(lengths[2])):
            validtriangles += 1

print(validtriangles)
