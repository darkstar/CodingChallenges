import re

def numat(x, y):
    foo = x + y - 1
    n = foo * (foo + 1) // 2
    r = n - (y - 1)
    return r

def nextcode(c):
    x = 252533 * c
    x = x % 33554393
    return x

with open("input.txt", mode="r") as f:
    line = f.readline().strip()
    y = int(re.search(r"row (\d+)", line).group(1))
    x = int(re.search(r"column (\d+)", line).group(1))

code = 20151125
pos = 1
codepos = numat(x, y)

while pos < codepos:
    code = nextcode(code)
    pos += 1

print(code)
