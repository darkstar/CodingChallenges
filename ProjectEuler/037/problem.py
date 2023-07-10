# we are given that we only need to find 11 numbers

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

def leftprime(n):
    mod = 10
    while True:
        if not isprime(n % mod):
            return False
        mod *= 10
        if mod > n:
            return True

def rightprime(n):
    while n > 0:
        if not isprime(n):
            return False
        n = n // 10
    return True

primes = []
for x in prime_generator():
    if x < 11:
        continue
    if leftprime(x) and rightprime(x):
        primes.append(x)
    if len(primes) == 11:
        break

print(sum(primes))
