import itertools

sums = set()

# to get a 9-digit "sum" x|y|z it's either a*bcde=fghi or ab*cde=fghi
# other combinations are not possible
for num in itertools.permutations("123456789"):
    n = "".join(num)
    x = int(n[0])
    y = int(n[1:5])
    z = int(n[5:])
    if x * y == z:
        sums.add(z)
    x = int(n[:2])
    y = int(n[2:5])
    # z remains
    if x * y == z:
        sums.add(z)

print(sum(sums))
