import re

def transpose(s):
    r = ""
    for x in range(len(s)):
        r += "0" if s[len(s) - x - 1] == "1" else "1"
    return r

with open("input.txt") as f:
    seed = f.readlines()[0].strip()

targetsize = 272

a = seed

while len(a) < targetsize:
    a = a + "0" + transpose(a)

a = a[:targetsize]

while True:
    # finish if odd
    if len(a) % 2 == 1:
        break
    # otherwise, fold together
    cksum = ""
    while len(a) > 0:
        h = a[:2]
        cksum += "1" if h[0] == h[1] else "0"
        a = a[2:]
    a = cksum

print(a)
