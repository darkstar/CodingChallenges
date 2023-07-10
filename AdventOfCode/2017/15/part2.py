with open("input.txt") as f:
    vals = list(map(lambda x: int(x[len(x) - 1]), map(lambda x: x.split(), f.readlines())))

s1 = vals[0]
s2 = vals[1]
matches = 0

for x in range(5000000):
    while True:
        s1 = (s1 * 16807) % 2147483647
        if s1 % 4 == 0:
            break

    while True:
        s2 = (s2 * 48271) % 2147483647
        if s2 % 8 == 0:
            break

    if (s1 ^ s2) & 0xffff == 0:
        matches += 1

print(matches)

