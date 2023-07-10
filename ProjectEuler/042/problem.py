def triangles(bound):
    t = []
    i = 1
    while True:
        tri = (i * (i + 1)) // 2
        if tri > bound:
            return t
        t.append(tri)
        i += 1

def wordsum(s):
    return sum(map(lambda x: ord(x)-ord('A')+1, s))

with open("input.txt", mode="r") as f:
    words = [ x.strip('"') for x in f.readline().split(",") ]

weights = list(map(wordsum, words))

# generate a sufficiently-large number of triangle numbers
tris = triangles(max(weights))

# filter all word weights that are in the list of triangular numbers
print(len(list(filter(lambda x: x in tris, weights))))

