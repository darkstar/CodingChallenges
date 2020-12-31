with open("input.txt", mode="r") as f:
    numbers = [int(x) for x in f.readlines()]
    
    cartesian = list((x, y, z) for x in numbers for y in numbers for z in numbers if x + y + z == 2020 and x <= y and y <= z)

    a, b, c = cartesian[0]

    print(a * b * c)

