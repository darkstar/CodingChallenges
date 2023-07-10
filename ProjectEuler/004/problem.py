import math

def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

p = 0

for x in range(1000):
    for y in range(x+1):
        if (is_palindrome(x*y) and (x * y > p)):
            p = x * y

print(p)
