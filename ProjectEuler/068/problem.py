import math

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#
#         d
#          \
#   a - b - c   f
#        |   \ /
#        i    e
#       / \  /
#      j    g
#            \
#             h
best = 0

# yes this should have been done by dynamic programming,
# but it's 2 AM and I'm tired and lazy ;-)

for a in nums:
    remaining1 = [x for x in nums if x != a]
    for b in remaining1:
        remaining2 = [x for x in remaining1 if x != b]
        for c in remaining2:
            remaining3 = [x for x in remaining2 if x != c]
            magic_sum = a + b + c
            for d in remaining3:
                # we want a to be the lowest number
                if d > a:
                    remaining4 = [x for x in remaining3 if x != d]
                    e = magic_sum - c - d
                    # do we have the number required?
                    if e in remaining4:
                        remaining5 = [x for x in remaining4 if x != e]
                        for f in remaining5:
                            if f > a:
                               remaining6 = [x for x in remaining5 if x != f]
                               g = magic_sum - e - f
                               if g in remaining6:
                                   remaining7 = [x for x in remaining6 if x != g]
                                   for h in remaining7:
                                       if h > a:
                                           remaining8 = [x for x in remaining7 if x != h]
                                           i = magic_sum - g - h
                                           if i in remaining8:
                                               remaining9 = [x for x in remaining8 if x != i]
                                               assert(len(remaining9) == 1)
                                               j = remaining9[0]
                                               if j + i + b == magic_sum and j > a:
                                                   s = "{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}".format(a, b, c,
                                                                                               d, c, e,
                                                                                               f, e, g,
                                                                                               h, g, i,
                                                                                               j, i, b)
                                                   if len(s) == 16 and int(s) > best:
                                                       best = int(s)

print(best)
