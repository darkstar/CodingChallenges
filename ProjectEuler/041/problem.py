import itertools

def isprime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if (n % 2 == 0 or n % 3 == 0):
        return False

    i = 5
    while i * i <= n:
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i += 6

    return True;

# since sum(1..9) and sum(1..8) are both divisible by 3, the numer we seek has 7 digits
maxprime = 0
for n in itertools.permutations("1234567"):
    num = int("".join(n))
    if isprime(num):
        maxprime = max(maxprime, num)

print(maxprime)
