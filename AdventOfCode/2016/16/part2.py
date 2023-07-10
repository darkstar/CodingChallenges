import re

def transpose(s):
    r = ""
    for x in range(len(s)):
        r += "0" if s[len(s) - x - 1] == "1" else "1"
    return r

with open("input.txt") as f:
    seed = f.readlines()[0].strip()

print("this might take a while...")

targetsize = 35651584

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
    for x in range(len(a) // 2):
        ch1 = a[2 * x]
        ch2 = a[2 * x + 1]
        cksum += "1" if a[2 * x] == a[2 * x + 1] else "0"

    a = cksum

print(a)
