import functools
import math

# we need fractions of the form (each var is <10)
# ab/bc = a/c
# so (10a+b) / (10b+c) == a/c or 9ac + bc = 10ab, also a!=b and all != 0

l = [ (10*a + b, 10*b+c) for a in range(1, 10) for b in range(1, 10) for c in range(1, 10) if a != b and 9*a*c+b*c==10*a*b ]

# multiply all fractions
frac = functools.reduce(lambda a, b: (a[0]*b[0], a[1]*b[1]), l, (1, 1))

# simplify fraction
gcd = math.gcd(frac[0], frac[1])
print(frac[1] // gcd)
