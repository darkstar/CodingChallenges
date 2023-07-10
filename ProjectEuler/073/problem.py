import math

def pfactors(n):
    factors = {}

    i = 2
    while i*i <= n:
        if (n % i == 0):
            n //= i
            factors[i] = 1 if i not in factors else factors[i] + 1
        else:
            i += 1

    if n > 1:
        factors[n] = factors[n] + 1 if n in factors else 1

    return factors

def phi(n):
    x = n 
    for p in pfactors(n):
        x *= (p - 1) 
        x //= p

    return x

def fracs(d):
    result = 0
    # 1/3 < x < 1/2 
    # start_numerator = d/3 + 1
    # end_numerator = d/2
    n = d // 3 + 1
    while n <= d // 2:
        if math.gcd(n, d) == 1:
            result += 1
        n += 1
    return result

# start with denominator 5, as d=1, 2, 3, 4 
# don't lie between 1/3 and 1/2
d = 5
result = 0
while d <= 12000:
    result += fracs(d)
    d += 1

print(result)
