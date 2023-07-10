def ispalindrome(n):
    s = str(n)
    return s == s[::-1]

def lychrel(n):
    for i in range(50):
        s = str(n)
        n = int(s) + int(s[::-1])
        if ispalindrome(n):
            return False
    return True

result = 0
for n in range(10001):
    if lychrel(n):
        result += 1

print(result)
