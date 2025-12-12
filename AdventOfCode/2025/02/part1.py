def in_range(x, a, b):
    return int(x) >= a and int(x) <= b

def fix_range(a, b):
    # check if start is off length
    if len(a) % 2 == 1:
        return "1" + "0" * len(a), b
    if len(b) % 2 == 1:
        return a, "9" * (len(b) - 1)
    return a, b

with open("input.txt") as f:
    ranges = [ x.split('-') for x in f.readline().strip().split(',') ]

# filter invalid ranges (odd length)
ranges = [ fix_range(a, b) for (a, b) in ranges if len(a) % 2 == 0 or len(b) % 2 == 0 ]

result = 0

# we are sure each number has even length at this point
for (a, b) in ranges:
    lstart = int(a[0:len(a)//2])
    lend = int(b[0:len(b)//2])
    a = int(a)
    b = int(b)
    for x in range(lstart, lend + 1):
        dbl = str(x) + str(x)
        if in_range(dbl, a, b):
            result += int(dbl)

print(result)
