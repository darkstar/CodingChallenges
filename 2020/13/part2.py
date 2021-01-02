from functools import reduce

def crt(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
 
 
def mul_inv(a, b):
    b0 = b
    x0 = 0
    x1 = 1

    if b == 1:
        return 1

    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0

    if x1 < 0:
        x1 += b0

    return x1

with open("input.txt", mode="r") as f:
    f.readline()
    times = list(map(lambda x: (int(x[0]), -x[1]), filter(lambda x: x[0] != "x", zip(f.readline().strip().split(","), range(100)))))

n = [ x[0] for x in times ]
a = [ x[1] for x in times ]

print(crt(n, a))
