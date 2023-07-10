import math

def ispent(n):
    h = (math.sqrt(24 * n + 1) + 1) / 6;
    return math.trunc(h) == h

n = 1
while True:
    m = 1
    while m <= n:
        dif = ((n - m) * (3 * m + 3 * n - 1)) // 2
        s = (3 * m * m - m + n * (3 * n - 1)) // 2
        if ispent(dif) and ispent(s):
            print(dif)
            exit(1)
        m += 1
    n += 1

