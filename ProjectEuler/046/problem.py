import math
import itertools

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

# 10000 primes should be enough
primes = list(itertools.islice(prime_generator(), 10000))

n = 7
while True:
    n += 2

    if isprime(n): # we only want composite numbers
        continue

    smallerprimes = [ x for x in primes if x < n ]
    found = False
    for p in smallerprimes:
        d = (n - p) // 2
        root = math.isqrt(d)
        if root * root == d:
            found = True
            break
    if not found:
        print(n)
        break

