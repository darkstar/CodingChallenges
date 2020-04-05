with open("input.txt") as f:
    lines = f.readlines()

total = 0

for l in lines:
    vals = list(map(int, l.strip().split()))
    total += max(vals) - min(vals)

print(total)
