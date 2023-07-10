# upper bound: 9999 * (1, 2)
# lower bound: 9 * (1, 2, 3, 4, 5)

def ispandigital(n): # sorry this is ugly...
    digits = {}
    for d in str(n):
        digits[d] = digits[d] + 1 if d in digits else 1
    return all(map(lambda x: int(x)>0 and int(x)<10, digits.keys())) and all(map(lambda x: x == 1, digits.values()))

# concatenate a number with its multiples (1, 2, ...) until a length of 9 or more is reached
def concat(n):
    k = 1
    s = ""
    while len(s) < 9:
        s = s + str(k * n)
        k += 1
    if len(s) > 9:
        return None
    return s

candidates = []

# TODO: we could skip all numbers that have any 0 in them
# this would also simplify ispandigital() as the first test could be removed
for x in range(1, 10000):
    s = concat(x)
    if s and ispandigital(s):
        candidates.append(int(s))

print(max(candidates))
