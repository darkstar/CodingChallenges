import math
import itertools
import functools
import operator

# our old and trusty prime generator

def prime_generator():
    D = {}
    q = 2
    while True:
        if not q in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D[p + q] = [p] if (p + q) not in D else D[p + q] + [p]
            del D[q]
        q += 1

# we only need primes up to ~7100 since 7100^2 + 2^3 + 2^4 > 50.000.000
primes = list(itertools.takewhile(lambda x: x < 7100, prime_generator()))
result = set()
limit = 50000000

for p2 in primes:
    s1 = p2 * p2
    if s1 > limit:
        break
    for p3 in primes:
        s2 = p3 * p3 * p3
        if s1 + s2 > limit:
            break
        for p4 in primes:
            s3 = p4 * p4 * p4 * p4
            if s1 + s2 + s3 <= limit:
                result.add(s1+s2+s3)
            else:
                break

print(len(result))
