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

def corners(n):
    if n == 1:
        return [1]
    last = n * n
    diff = n - 1
    return [ last - 3 * diff, last - 2 * diff, last - diff, last ]

i = 3 
total = 1
primes = 0
while True:
    next = corners(i)
    p = [ x for x in next if isprime(x) ]

    total += len(next)
    primes += len(p)

    if 10 * primes < total:
        print(i)
        break

    i += 2
