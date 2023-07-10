import math
import itertools

# assume solution has 6 digits

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

primes = list(filter(lambda y: y > 99999, itertools.takewhile(lambda x: x < 1000000, prime_generator())))

for p in primes:
    ps = str(p)
    for x in "12": # digit to replace (1..2 is enough since we need 8 hits among 1..9)
        if not x in ps:
            continue
        pcount = 0
        for r in "123456789": # digit to replace it with
            np = int(ps.replace(x, r))
            if np in primes:
                pcount += 1
        if pcount == 8:
            print(p)
            exit(1)

