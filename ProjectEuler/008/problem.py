import math

with open("input.txt", mode="r") as f:
    num = "".join([ x.strip() for x in f.readlines() ])

n = 13
result = 0

for x in range(1000 - n + 1):
    slice = num[x:x + n]
    v = math.prod(map(lambda x: int(x), slice))
    if v > result:
        result = v

print(result)
