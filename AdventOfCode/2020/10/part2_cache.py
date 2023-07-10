from functools import lru_cache


with open("input.txt", mode="r") as f:
    jolts = [ int(x.strip()) for x in f.readlines() ]

jolts.sort()

jolts = [0] + jolts + [ jolts[-1] + 3]

@lru_cache
def counts(j):
    global jolts
    if j == 0:
        return 1
    c1, c2, c3 = 0, 0, 0
    return (counts(j - 3) if (j - 3) in jolts else 0) + \
           (counts(j - 2) if (j - 2) in jolts else 0) + \
           (counts(j - 1) if (j - 1) in jolts else 0)

print(counts(jolts[-1]))
