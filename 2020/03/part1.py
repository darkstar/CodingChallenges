with open("input.txt", mode="r") as f:
    m = [x.strip() for x in f.readlines()]

width = len(m[0])
height = len(m)

cx = 0
cy = 0

trees = 0

while cy < height:
    field = m[cy][cx % width]
    
    if field == "#":
        trees += 1

    cx += 3
    cy += 1

print(trees)

