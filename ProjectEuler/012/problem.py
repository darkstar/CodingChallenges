import math
import functools

def tri(n):
    return (n * (n + 1)) // 2

@functools.lru_cache(maxsize=100000)
def divisors(n):
    i = 1
    d = 0
    while i * i <= n:
        if n % i == 0:
            d += 2 
        i += 1
    return d

i = 100 # arbitrary starting number
while True:
    if divisors(tri(i)) > 500:
        print(tri(i))
        break
    i += 1
