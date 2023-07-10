result = 0

for n in range(1, 30):
    i = 1 
    while True:
        s = str(i ** n)
        if len(s) > n:
            break
        if len(s) == n:
            result += 1
        i += 1

print(result)
