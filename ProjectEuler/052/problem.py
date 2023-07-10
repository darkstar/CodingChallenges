for x in range(100000, 1000000//6):
    s1 = set(str(x))
    if set(str(2 * x)) != s1:
        continue
    if set(str(3 * x)) != s1:
        continue
    if set(str(4 * x)) != s1:
        continue
    if set(str(5 * x)) != s1:
        continue
    if set(str(6 * x)) != s1:
        continue
    print(x)
    break
