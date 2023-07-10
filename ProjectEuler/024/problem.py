import itertools

n = itertools.permutations("0123456789", 10)
print("".join(list(itertools.islice(n, 999999, 1000000))[0]))

