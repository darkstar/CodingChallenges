with open("input.txt") as f:
    l = [ int(x[1:]) if x[0] == 'R' else -int(x[1:]) for x in f.readlines()]

p = 50
result = 0

for x in l:
    p = p + x
    while p >= 100:
        p -= 100
        result +=1
    while p < 0:
        p += 100
        result += 1

print(result)
