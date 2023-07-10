result = 0

for a in range(1, 100):
    for b in range(1, 100):
        ds = sum(map(int, str(a**b)))
        result = max(result, ds)

print(result)
