import math
import functools

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


def divisors(n):
    if (n == 1):
        return [1]

    factors = [ [a, b] for (a, b) in pfactors(n).items() ]
    f = [0] * len(factors) # powers
    divisors = []
    while True:
        divisors.append(functools.reduce(lambda x, y: x*y, [factors[x][0]**f[x] for x in range(len(factors))], 1))
        i = 0
        # go to next combination
        while True:
            f[i] += 1
            if f[i] <= factors[i][1]:
                break;
            f[i] = 0
            i += 1
            if i >= len(factors):
                return divisors

amicable = 0

for i in range(2, 10001):
    a = sum(divisors(i)) - i # "- i" because we only want proper divisors
    b = sum(divisors(a)) - a
    if a != b and b == i:
        amicable += a # we get the other number later anyways so we only need to count one now

print(amicable)
