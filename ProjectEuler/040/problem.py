s = ""
i = 1
n = 1

result = 1

while True:
    if i > 1000000:
        break

    if len(s) == 0:
        # add next number to string
        s += str(n)
        n += 1

    # pick digit
    d = s[0]
    s = s[1:]
    if i in [1, 10, 100, 1000, 10000, 100000, 1000000]:
        result *= int(d)

    i += 1

print(result)
