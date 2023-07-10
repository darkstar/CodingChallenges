import math

def pfactors(n):
    factors = {}

    i = 2
    while i*i <= n:
        if (n % i == 0):
            n //= i
            factors[i] = 1 if i not in factors else factors[i] + 1
        else:
            i += 1

    if n > 1:
        factors[n] = factors[n] + 1 if n in factors else 1

    return factors

found = []

n = 647
while True:
    if len(pfactors(n)) == 4:
        found.append(n)
    else:
        found = []

    if len(found) == 4:
        print(found[0])
        break

    n += 1
