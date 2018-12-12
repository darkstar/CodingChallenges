# observation:
# number of presents for house n = 10 * sigma(n)
# with sigma: sum of divisors of n
# OEIS A000203
# we know:
#   sigma(n) < n*sqrt(n) ==> n > sigma(n)^(2/3)
#   sigma(n) > n+sqrt(n)

import math
from collections import defaultdict
from functools import reduce

target = 0
startvalue = 0

def factor(n):
    i = 2
    limit = math.sqrt(n)
    while i <= limit:
      if n % i == 0:
        yield i
        n = n / i
        limit = math.sqrt(n)
      else:
        i += 1
    if n > 1:
        yield n

def factorGenerator(n):
    d=defaultdict(int)
    for f in factor(n):
        d[f]+=1
    return [(e,d[e]) for e in sorted(d.keys())]

def divisorGen(n):
    factors = list(factorGenerator(n))
    nfactors = len(factors)
    f = [0] * nfactors
    while True:
        yield reduce(lambda x, y: x*y, [factors[x][0]**f[x] for x in range(nfactors)], 1)
        i = 0
        while True:
            f[i] += 1
            if f[i] <= factors[i][1]:
                break
            f[i] = 0
            i += 1
            if i >= nfactors:
                return

with open('input.txt', mode='r') as f:
    target = int(f.readlines()[0].rstrip()) // 10

startvalue = int(pow(target, 2/3))

print('Testing from {}'.format(startvalue))

x = startvalue

while True:
    s = sum(divisorGen(x))
    if (x % 100000 == 0): print(x, 10*s)
    if s > target: break
    x += 1

print("Solution: {}".format(x))

