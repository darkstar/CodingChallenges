from decimal import Decimal, getcontext
import math

getcontext().prec = 105 

def sqrsum(n):
    s = str(Decimal(n).sqrt())[:101] # add 1 for the decimal point
    return sum([int(x) for x in s if x != "."])

s = 0
for x in range(2, 101):
    sq = int(math.sqrt(x))
    if sq * sq == x:
        continue
    s += sqrsum(x)

print(s)
