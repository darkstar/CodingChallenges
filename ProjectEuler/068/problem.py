import math

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

# the indices for the unique string that defines the ring
idx = [ 0, 1, 2, 3, 2, 4, 5, 4, 6, 7, 6, 8, 9, 8, 1 ]

best = 0

def isvalid(ring):
    if len(ring) <= 3:
        return True
    magic_sum = ring[0] + ring[1] + ring[2]
    if len(ring) >= 5:
        if ring[2] + ring[3] + ring[4] != magic_sum or ring[3] < ring[0]:
            return False
    if len(ring) >= 7:
        if ring[4] + ring[5] + ring[6] != magic_sum or ring[5] < ring[0]:
            return False
    if len(ring) >= 9:
        if ring[6] + ring[7] + ring[8] != magic_sum or ring[7] < ring[0]:
            return False
    if len(ring) == 10:
        if ring[8] + ring[9] + ring[1] != magic_sum or ring[9] < ring[0]:
            return False
    return True

def search(ring, digits):
    global best

    # check if the n-gon ring meets all criteria
    # if not, prune the search tree here
    if not isvalid(ring):
        return

    # if the ring has length 10, we have found a candidate
    if len(ring) == 10:
        s = "".join([ str(ring[i]) for i in idx])
        if len(s) == 16 and int(s) > best:
            best = int(s)
        return

    # assume at least one digit left to pick
    assert(len(digits) > 0)

    # go through all digits and form a new ring with them
    for i in range(len(digits)):
        # take a digit from the list
        d = digits[i]
        rest = digits[:i] + digits[i+1:]
        # recursively descend
        search(ring + [d], rest)

search([], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(best)
