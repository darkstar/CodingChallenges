import math

a = 0
b = 1
s = 0

while True:
    n = a + b
    a = b
    b = n

    if (n % 2 == 0):
        s += n

    if (n > 4000000):
        break

print(s)

