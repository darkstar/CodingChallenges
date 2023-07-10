import math

def dsum(n):
    res = 0
    while n > 0:
        res += math.factorial(n % 10)
        n = n // 10
    return res

# maximum upper bound: 9999999 because: 7*9! < 9999999
# upper bound (my rough guess): 100000 (yes, it's enough ;-)

result = 0

for n in range(10, 100000):
    if n == dsum(n):
        result += n

print(result)
