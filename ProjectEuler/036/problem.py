def is_palindrome(n):
    s = str(n)
    t = str(bin(n)[2:])
    return s == s[::-1] and t == t[::-1]

s = 0

for i in range(1000001):
    if is_palindrome(i):
        s += i

print(s)
