# ref. https://en.wikipedia.org/wiki/Primality_test
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

def numprimes(a, b):
    n = 0
    while True:
        x = n * n + a * n + b
        if not isprime(x):
            return n
        n += 1

maxprimes = 0
maxa = 0
maxb = 0

for a in range(-1000, 1001):
    for b in range(-1000, 1001):
        p = numprimes(a, b)
        if p > maxprimes:
            maxprimes = p
            maxa = a
            maxb = b
print(maxa * maxb)
