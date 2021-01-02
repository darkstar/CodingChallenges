def nocc(seats, x, y, w, h, dx, dy):
    while True:
        x += dx
        y += dy
        if x < 0 or y < 0 or x >= w or y >= h:
            return 0
        if seats[y][x] == 'L':
            return 0
        if seats[y][x] == '#':
            return 1

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
            occupied = sum(list(map(lambda n: nocc(seats, x, y, w, h, n[0], n[1]), neighbors)))
            old = seats[y][x]
            if old == 'L' and occupied == 0:
                new[y][x] = '#'
                changes += 1
            elif old == '#' and occupied >= 5:
                new[y][x] = 'L'
                changes += 1
            else:
                new[y][x] = old
    if changes == 0:
        break
    seats = new

print(("".join(["".join(x) for x in seats])).count("#"))
