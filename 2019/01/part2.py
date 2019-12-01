totalweight = 0

# the fuel required cannot be negative
def fuel(weight):
    return max(0, x // 3 - 2)

with open("input.txt", mode="r") as f:
    # for each module...
    for line in f.readlines():
        # get the module weight
        x = int(line.strip())
        # this will be the total fuel for this module
        totalfuel = 0
        # as long as the fuel required is non-negative:
        while fuel(x) > 0:
            # store required fuel for this module...
            totalfuel += fuel(x)
            # and loop again for the fuel required to lift this fuel weight
            x = fuel(x)

        # store the total fuel required for this module
        totalweight += totalfuel

print(totalweight)
