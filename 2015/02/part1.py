import re

with open('input.txt', mode='r') as f:
    presents = [(int(v[0]), int(v[1]), int(v[2])) for v in [l.split('x', 3) for l in f.readlines()]]

    areasizes = [(x*y, x*z, y*z) for (x,y,z) in presents]

    totalareasizes = [ 2*s[0] + 2*s[1] + 2*s[2] + min(s) for s in areasizes ]

print(sum(totalareasizes))
