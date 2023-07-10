# Since phi(n) = n * PROD(1 - 1/p) over all prime divisors of n,
# we see that n/phi(n) = PROD(p / (p - 1)) for all primes dividing n
#
# this product will be maximized if the primes p are the smallest
# possible primes.
#
# So all we need to do is multiply the primes, starting with 2,
# until we find the largest product that still fits under our
# limit of 1000000. That product of primes will maximize n/phi(n)

import math

primes = [ 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 53, 59, 61 ]

s = [x for x in map(lambda x: math.prod(primes[:x]), range(len(primes))) if x < 1000000]

print(s[-1])
