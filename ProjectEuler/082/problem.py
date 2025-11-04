with open("input.txt", mode="r") as f:
    m = [ [ int(n) for n in x.split(",") ] for x in f.readlines() ]

def path(m, ypos):
    d = len(m)

    # the path matrix
    p = [ [ 999999999 for x in range(d) ]  for y in range(d) ]
    p[ypos][-1] = m[ypos][-1]

    # reverse path search by calculating the minimum distance to
    # the end
    # TODO: instead of walking over the whole matrix, we could only walk
    # over the anti-diagonal from bottom-right to top-left. but this is
    # fast enough for now ;-)
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
    v = [ y[0] for y in p ]
    return min(v)

# stupid brute force solution but it's still faster than 1 minute ;-)
# just calculate all 80 paths and chose the smallest one
lens = [ path(m, i) for i in range(len(m)) ]
print(min(lens))
