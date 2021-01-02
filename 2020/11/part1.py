with open("input.txt", mode="r") as f:
    seats = [ list(row.strip()) for row in f.readlines() ]

w = len(seats[0])
h = len(seats)

neighbors = [ (-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1) ]

while True:
    changes = 0
    new = [ list("." * w) for i in range(h) ]
    for y in range(h):
        for x in range(w):
            tmp = list(map(lambda c: (x + c[0], y + c[1]), neighbors))
            n = list(filter(lambda a: a[0] >= 0 and a[1] >= 0 and a[0] < w and a[1] < h, tmp))
            v = list(map(lambda a: seats[a[1]][a[0]], n))
            occupied = v.count('#')
            old = seats[y][x]
            if old == 'L' and occupied == 0:
                new[y][x] = '#'
                changes += 1
            elif old == '#' and occupied >= 4:
                new[y][x] = 'L'
                changes += 1
            else:
                new[y][x] = old
    if changes == 0:
        break
    seats = new

print(("".join(["".join(x) for x in seats])).count("#"))
