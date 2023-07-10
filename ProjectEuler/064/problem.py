import math

def period(n):
    a = math.isqrt(n)
    b = 1
    rem = {}
    if a * a == n:
        return 0

    i = 1
    while True:
        b = (n - (a * a)) / b
        f = int((math.sqrt(n) + a) / b)
        a = (f * b) - a
        if (a, b) in rem:
            return i - rem[a, b]
        rem[a, b] = i
        i += 1

result = 0

for n in range(1, 10000):
    if period(n) % 2 == 1:
        result += 1

print(result)
