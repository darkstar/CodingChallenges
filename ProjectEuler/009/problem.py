import math

# a is the smallest number so it is at maximum 1000/3
for a in range(1, 1000 // 3):
    # b is the second smalles number which can go from a+1 to (1000-a)/2
    for b in range(a + 1, (1000 - a) // 2):
        # c is the remaining side
        c = 1000 - a - b
        if c * c == a * a + b * b:
            print(a*b*c)
            break

