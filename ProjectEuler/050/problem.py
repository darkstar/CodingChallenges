import itertools

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

primes = list(itertools.takewhile(lambda x: x < 1000000, prime_generator()))

bestlen = 0
bestprime = 0

for l in range(len(primes)):
    if l + bestlen > 1000: # don't bother to find any longer chains
        break
    for r in range(l, len(primes)):
        if r - l < bestlen: # don't bother to check this short chain
            continue
        s = sum(primes[l:r])
        if s > 1000000:
            break
        if s in primes:
            if r - l > bestlen:
                bestlen = r - l
                bestprime = s

print(bestprime)
