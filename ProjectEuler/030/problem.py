def digitsum(n, p):
    s = 0
    while n > 0:
        s += (n % 10) ** p
        n = n // 10
    return s

result = 0

for n in range(2, 6*(9**5) + 1):
    d = digitsum(n, 5)
    if d == n:
        result += d

print(result)
