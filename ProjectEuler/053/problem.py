import math

result = 0
for n in range(23, 101):
    for r in range(1, n):
        if math.comb(n, r) > 1000000:
            result += 1

print(result)
