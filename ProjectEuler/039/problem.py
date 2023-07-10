import math

results = {}

# brute force, because it's late and it is still fast enough ;-)
for p in range(1, 1000):
    for a in range(1, p // 4 + 1):
        for b in range(a + 1, (p - a) // 2 + 1):
            c = math.sqrt(a*a+b*b)
            if a + b + c == p:
                results[p] = results[p] + 1 if p in results else 1

print(max(results, key=results.get))
