with open("input.txt") as f:
    l = [ int(x[1:]) if x[0] == 'R' else -int(x[1:]) for x in f.readlines()]

p = 50
result = 0

for x in l:
    p = (p + x) % 100
    if p == 0:
        result += 1

print(result)
