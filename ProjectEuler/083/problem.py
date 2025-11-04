with open("input.txt", mode="r") as f:
    m = [ [ int(n) for n in x.split(",") ] for x in f.readlines() ]

d = len(m)

# the path matrix
p = [ [ 999999999 for x in range(d) ]  for y in range(d) ]
p[-1][-1] = m[-1][-1]

# reverse path search by calculating the minimum distance to
# the end
while True:
    changed = 0
    for y in range(d):
        for x in range(d):
            o = p[y][x]
            n = o
            if y < d-1:
                n = min(n, m[y][x] + p[y+1][x])
            if y > 0:
                n = min(n, m[y][x] + p[y-1][x])
            if x < d-1:
                n = min(n, m[y][x] + p[y][x+1])
            if x > 0:
                n = min(n, m[y][x] + p[y][x-1])
            if n != o:
                changed += 1
                p[y][x] = n
    if changed == 0:
        break

print(p[0][0])

