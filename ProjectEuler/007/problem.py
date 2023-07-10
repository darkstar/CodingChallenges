import math
import itertools

# prime generator, adapted from http://code.activestate.com/recipes/117119/

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

print(list(itertools.islice(prime_generator(), 10000, 10001))[0])

