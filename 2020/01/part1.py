with open("input.txt", mode="r") as f:
    numbers = [int(x) for x in f.readlines()]
    
    cartesian = list((x, y) for x in numbers for y in numbers if x + y == 2020 and x <= y)

    a, b = cartesian[0]

    print(a * b)

