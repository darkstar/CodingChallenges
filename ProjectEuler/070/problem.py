# in order to minimize n/phi(n), we need to maximize phi(n).
# phi(n) is maximized if n is a prime, then phi(n) = n - 1.
# A prime x can never be a permutation of x-1 since that only
# changes the last digit.
# So we have no solutions which are prime numbers
# The next best solution is a product of 2 primes which are
# closely together, since phi(a * b) = phi(a) * phi(b)
# if that doesn't find any permutations, try 3 primes, etc.
#
# Method: find enough primes close to sqrt(1e7) and multiply
# them, checking for permutations

import itertools

def isperm(a, b):
    return "".join(sorted(str(a))) == "".join(sorted(str(b)))

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

# we arbitrarily limit ourselves to primes above 1000 and below 5000
# sqrt(10000000) is roughly 3160, so we search around that value
primes = list(itertools.dropwhile(lambda x: x < 1000, itertools.takewhile(lambda x: x <= 5000, prime_generator())))

# find all numbers that are a permutation of their phi(n) from the list of multiplications
# and have a product smaller than 1000000
mult = filter(lambda k: k[0] < 10000000 and isperm(k[0], k[1]), 
              map(lambda x: (x[0] * x[1], (x[0] - 1) * (x[1] - 1)), 
                  itertools.combinations_with_replacement(primes, 2)))

# now sort the array by n/phi(n). The solution is the first element

s = sorted(mult, key=lambda x: x[0] / x[1] )
print(s[0][0])
