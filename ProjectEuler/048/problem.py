s = 0

for n in range(1, 1001):
    s += n**n

print(s % 10000000000)
