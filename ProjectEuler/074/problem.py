import math
import itertools

def fact(n):
    return 1 if n < 2 else n * fact(n-1)

facts = list(map(lambda x: fact(x), range(10)))

def digitfact(n):
    res = 0
    while n > 0:
        res += facts[n % 10]
        n //= 10
    return res

# this can be optimized by saving the length of the found chains
# but I'm lazy and it runs in < 30s so I won't bother
def chainlen(n, ch=[]):
    if n in ch:
        return len(ch)

    next = digitfact(n)

    return chainlen(next, ch + [n])

n = 1
result = 0

while n < 1000000:
    c = chainlen(n)
    if c == 60:
        result = result + 1
    n += 1


print(result)
