import math

chainlengths = { 1: 1 }

def chainlength(n):

    if n in chainlengths:
        return chainlengths[n]

    if n % 2 == 0:
        newlength = chainlength(n // 2) + 1
    else:
        newlength = chainlength(3 * n + 1) + 1

    chainlengths[n] = newlength

    return newlength

maxlen = 0
result = 0

i = 2
while i < 1000000:
    n = chainlength(i)
    if n > maxlen:
        result = i
        maxlen = n

    i += 1

print(result)
