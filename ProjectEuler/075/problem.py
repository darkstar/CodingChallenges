import math

# use euklid's generating function for pthagorean triples
# scale them up as needed until the perimeter exceeds 1500000

def triple_generator():
    m = 1
    while True:
        for n in range(1, m):
            if (m + n) % 2 == 1 and math.gcd(m, n) == 1:
                a = m * m - n * n
                b = 2 * m * n
                yield a, b, m * m + n * n, 2 * m * (m + 1)
        m += 1

tri = {}

for a, b, c, s in triple_generator():
    if s > 1500000:
        break
    p = a + b + c
    for n in range(p, 1500001, p):
        tri[n] = 1 if n not in tri else tri[n] + 1

print(len([x for x in tri.values() if x == 1]))
