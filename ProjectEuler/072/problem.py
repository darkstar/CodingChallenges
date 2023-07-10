# for each denominator d we have phi(d) possible
# numerators. Simply add them all up
import itertools

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

def phi(n):
    x = n 
    for p in pfactors(n):
        x *= (p - 1) 
        x //= p

    return x

d = 2
result = 0
while d <= 1000000:
    result += phi(d)
    d += 1

print(result)
