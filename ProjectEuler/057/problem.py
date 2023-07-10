from fractions import Fraction

result = 0

f = Fraction(1, 2)
for i in range(1000):
    x = 1 + f
    dn = len(str(x.numerator))
    dd = len(str(x.denominator))
    if dn > dd:
        result += 1
    f = 1 / (2 + f)

print(result)
