with open("input.txt", mode="r") as f:
    l = [ x.strip().split() for x in f.readlines() ]

def sgn(x):
    if x < 0:
        return -1
    if x > 0:
        return 1
    return 0

moves = "".join([ x[0] * int(x[1]) for x in l ])

h = (0, 0)
t = (0, 0)

d = { "R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1) }

visited = set( t )

for m in moves:
    h = (h[0] + d[m][0], h[1] + d[m][1])
    dx, dy = h[0] - t[0], h[1] - t[1]
    #print("head {}, tail {}".format(h, t))
    if abs(dx) < 2 and abs(dy) < 2:
        continue

    m = (sgn(dx),sgn(dy))
    #print("  tail moves {}".format(m))
    t = (t[0] + m[0], t[1] + m[1])

    visited.add(t)

print(len(visited))
