import math

# each path consists of 20 "right" and 20 "down" movements, in arbitrary order
# since we only need to find the positions of the "right" movements
# we can use 20+20 choose 20 (the order in which we choose them doesn't matter)

print(math.comb(40, 20))

