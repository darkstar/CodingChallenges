import re

with open('input.txt', mode='r') as f:
    presents = [(int(v[0]), int(v[1]), int(v[2])) for v in [l.split('x', 3) for l in f.readlines()]]

    circumferences = [(x+x+y+y, x+x+z+z, y+y+z+z) for (x,y,z) in presents]

    mincircumferences = [min(a) for a in circumferences]

    volumes = [x*y*z for (x,y,z) in presents]

    ribbonlength = [a[0] + a[1] for a in zip(mincircumferences, volumes)]

print(sum(ribbonlength))
