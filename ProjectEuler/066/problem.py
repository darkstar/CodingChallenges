import math

pmax = 0
result = 0

for d in range(2, 1001):
    sq = math.isqrt(d)

    if sq * sq == d:
        continue

    # continuous fractions -> i'th convergent is a solution
    # braindead implementation of pell's equation (since it's 3AM and I'm tired...)
    m = 0
    x = 1
    a = sq

    num = a
    den = 1

    num1 = 1
    den1 = 0

    while num * num - d * den * den != 1:
        m = x * a - m
        x = (d - m * m) // x
        a = (sq + m) // x

        num2, num1 = num1, num
        den2, den1 = den1, den

        num = a * num1 + num2
        den = a * den1 + den2

    if num > pmax:
        pmax = num
        result = d

print(result)
