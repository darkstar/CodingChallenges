import itertools
import functools

def ilog10(n):
    if n < 10:
        return 0
    if n < 100:
        return 1
    if n < 1000:
        return 2
    if n < 10000:
        return 3
    if n < 100000:
        return 4
    print("error")
    exit(1)

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

@functools.cache
def isprime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if (n % 2 == 0 or n % 3 == 0):
        return False

    i = 5
    while i * i <= n:
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i += 6

    return True;        


# assume our primes are no larger than 4 digits...
primes = list(itertools.takewhile(lambda x: x < 10000, prime_generator()))

pairs = {}

# build pairs of concatenatable primes
for a in primes:
    for b in primes:
        if b == a:
            continue
        candidate = a * (10 ** (ilog10(b) + 1)) + b
        if not isprime(candidate):
            continue
        candidate = b * (10 ** (ilog10(a) + 1)) + a
        if not isprime(candidate):
            continue
        pairs[ (a, b) ] = True

for a, b in pairs:
    for c in [x for x in primes if a != x and b != x and (a, x) in pairs and (b, x) in pairs]:
        for d in [x for x in primes if a != x and b != x and c != x and (a, x) in pairs and (b, x) in pairs and (c, x) in pairs]:
            for e in [x for x in primes if a != x and b != x and c != x and d != x and \
                    (a, x) in pairs and (b, x) in pairs and (c, x) in pairs and (d, x) in pairs]:
                print(a + b + c + d + e)
                break

