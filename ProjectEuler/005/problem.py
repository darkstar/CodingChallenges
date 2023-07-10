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

allfactors = {}

for x in range(2, 21):
    for k, v in pfactors(x).items():
        allfactors[k] = max(allfactors[k] if k in allfactors else 0, v)

result = 1

for k, v in allfactors.items():
    result *= k ** v

print(result)
