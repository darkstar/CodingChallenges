import math

# using Euler's recurrence formula from
# https://mathworld.wolfram.com/PartitionFunctionP.html

cache = {0: 1}

def Pn(n):
    global cache

    if n < 0:
        return 0

    if n in cache:
        return cache[n]

    p = 0
    for k in range(1, n + 1):
        x = n - k * (3 * k - 1) // 2;
        y = n - k * (3 * k + 1) // 2;

        p1 = Pn(x)
        p2 = Pn(y)

        if k % 2 == 1:
            p += p1 + p2
        else:
            p -= p1 + p2

    cache[n] = p
    return p

# subtract one, because the solution asks for "at least 2 integers"
print(Pn(100) - 1)
