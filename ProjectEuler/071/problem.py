import math

best = (0, 1)

d = 2
while d < 1000000:
    # calculate the largest n/d with that denominator
    # that is below 3/7
    # n/d < 3/7 -> 7*n < 3*d -> n < 3*d/7 (or n = floor((3*d-1)/7) )
    n = math.floor((3 * d - 1) / 7)
    if n/d > best[0]/best[1]:
        best = (n, d)

    d += 1

print(best[0])
