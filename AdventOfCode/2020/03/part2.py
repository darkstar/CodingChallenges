with open("input.txt", mode="r") as f:
    m = [x.strip() for x in f.readlines()]

width = len(m[0])
height = len(m)

result = 1

slopes= [ (1, 1), (3, 1), (5, 1), (7, 1), (1, 2) ]

for dx, dy in slopes:
    trees = 0
    cx = 0
    cy = 0
    while cy < height:
        field = m[cy][cx % width]
        
        if field == "#":
            trees += 1
    
        cx += dx
        cy += dy

    result *= trees

print(result)
