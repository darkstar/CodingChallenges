from fractions import Fraction

def seq(n):
    if n == 1:
        return 2
    if n % 3 == 0:
        return 2 * (n // 3)
    return 1

def cfr(x, n = Fraction(1)):
    if n > x:
        return Fraction(1)
    return seq(n) + (1 / cfr(x, n + 1))

print(sum(map(int,list(str(cfr(Fraction(99)).numerator)))))

