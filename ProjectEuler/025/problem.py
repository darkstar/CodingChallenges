fibs = {}

def fib(n):
    if n in fibs:
        return fibs[n]

    if n <= 2:
        return 1

    x = fib(n - 1) + fib(n - 2)
    fibs[n] = x
    return x

i = 1
while True:
    s = str(fib(i))
    if len(s) >= 1000:
        print(i)
        break
    i += 1
