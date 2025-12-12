def in_range(x, a, b):
    return int(x) >= a and int(x) <= b

def fix_range(a, b):
    # if start and end are bot same parity, just return the range as-is
    if len(a) % 2 == len(b) % 2:
        return [(a, b)]
    # if start is odd and end is even:
    if len(a) % 2 == 1:
        return [(a, "9" * (len(a))), ("1" + "0" * len(a), b)]
    # if start is even and end is odd
    if len(b) % 2 == 1:
        return [(a, "9" * (len(b) - 1)), ("1" + "0" * len(a), b)]
    # should not happen
    return None

with open("input.txt") as f:
    ranges = [ x.split('-') for x in f.readline().strip().split(',') ]

# split ranges (so that all ranges have the same length of members)
ranges = [ fix_range(a, b) for (a, b) in ranges ]
# flatten the list
ranges = sum(ranges, [])

candidates = set()

for r in ranges:
    # the length of the number
    l = len(r[0])
    # for all divisors of l (including 1, excluding l)
    for i in range(1, l):
        if l % i != 0:
            continue
        # candidate of length i
        cstart = r[0][:i]
        cend = r[1][:i]
        # try all possible invalid numbers
        for k in range(int(cstart), int(cend) + 1):
            s = str(k) * (l // i)
            if in_range(int(s), int(r[0]), int(r[1])):
                candidates.add(s)

result = 0
for s in candidates:
    result += int(s)

print(result)
