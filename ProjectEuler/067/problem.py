# this is the same code as in problem 18!

import math

with open("input.txt", mode="r") as f:
    t = [ list(map(int, x.strip().split(" "))) for x in f.readlines() ]

t.reverse()

for i in range(1, len(t)):
    # we need the n'th row and the n+1'th row
    row = t[i]
    prev = t[i - 1]

    # for every number in the n'th row...
    for x in range(len(row)):
        # we add the larger of the two numbers in the row below it
        v = max(prev[x], prev[x + 1])
        row[x] = row[x] + v

# in the end the last row contains the maximum path length as its only element
print(*t[-1])
