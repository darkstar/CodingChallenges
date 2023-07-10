import math
import itertools
import functools
import operator

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

print(functools.reduce(operator.add, itertools.takewhile(lambda x: x < 2000000, prime_generator()), 0))

