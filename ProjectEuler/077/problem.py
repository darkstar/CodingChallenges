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

# 100 primes should be enough
primes = list(itertools.islice(prime_generator(), 100))

# We do this recursively, with memoization
# for each number, we subtract all primes smaller than that number, and
# recursively call the function with the remainder
# We will get duplicates that way (e.g. 10 will recursively call into
# count(10-3) and count(10-7), which yields 10=7+3 and 10=3+7, which are
# different lists.
# to Counteract that, we don't store those lists (so we don't have to
# sort/filter them), but rather we store the multiplication of all the
# primes that make up that number in a set, which neatly eliminates
# duplicates. So count(10) will store 7*3, 5*5, 2*2*2*2*2, 2*2*3*3 and
# 5*3*2
# This list will be stored in the memoization, keyed by the number n,
# as we can re-use it for later calls with larger numbers
mem = {}
def count(n):
    ids = set()
    if n in mem:
        return mem[n]

    if n == 0:
        return ids
    for p in primes:
        if p == n:
            ids.add(n)
        if p >= n:
            break
        prev = count(n - p)
        otherids = [ i * p for i in prev]
        for x in otherids:
            ids.add(x)
    mem[n] = ids
    return ids


n = 10 # start here
while True:
    x = len(count(n))
    if x > 5000:
        print(n)
        break
    n += 1
