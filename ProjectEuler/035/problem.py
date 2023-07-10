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

def allprime(p):
    s = str(p)
    l = len(s)
    s = s * 2
    for x in range(1, l):
        if not isprime(int(s[x:x+l])):
            return False
    return True

found = 0
for p in prime_generator():
    if p > 1000000:
        break
    if allprime(p):
        found += 1

print(found)
