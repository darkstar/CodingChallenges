import math

m = 1
result = 0

def is_square(n):
    v = int(math.sqrt(n))
    return v * v == n

# brute force solution
# yes it's slow but it still only takes 3 minutes or so

while True:
    for a in range(1, m + 1):
        for b in range(1, a + 1):
            shortest = (a+b)*(a+b)+m*m
            if is_square(shortest):
                result = result + 1
    if result > 1000000:
        break
    print("m =", m, "total =", result)
    m = m + 1

print(m)
