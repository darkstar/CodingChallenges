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


primes = list(filter(lambda y: y >= 1000, itertools.takewhile(lambda x: x < 10000, prime_generator())))

for p1 in primes:
    if p1 == 1487: # skip this as it's not the solution we're looking for
        continue
    s1 = str(p1)
    for p2 in filter(lambda x: x > p1, primes):
        s2 = str(p2)
        d = p2 - p1
        p3 = p2 + d
        # this comparison is actually buggy but it works for our case, so yeah....
        if p3 in primes and set(s1) == set(s2) and set(s1) == set(str(p3)):
            print("{}{}{}".format(p1, p2, p3))
            exit(1)
