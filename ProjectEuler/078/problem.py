import math

cache = {0: 1}

def p_mod(n):
    if n in cache:
        return cache[n]

    result = 0
    k = 1
    sign = 1

    while True:
        x = (k * (3 * k - 1)) // 2
        y = (k * (3 * k + 1)) // 2

        if x > n:
            break
        result += sign * p_mod(n - x)

        if y > n:
            break
        result += sign * p_mod(n - y)

        k += 1
        sign = -sign;

    cache[n] = result
    return result

n = 10
while True:
    if p_mod(n) % 1000000 == 0:
        print(n)
        break
    n += 1

