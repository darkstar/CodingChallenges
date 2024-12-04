import re

def calc(x):
    v = re.match(r"mul\((\d+),(\d+)\)", x)
    a = int(v.group(1))
    b = int(v.group(2))
    return a * b

with open("input.txt", mode="r") as f:
    code = f.readlines()

muls = []
for l in code:
    muls += re.findall(r"mul\(\d{1,3},\d{1,3}\)", l)

result = 0

prods = list(map(lambda x: calc(x), muls))

print(sum(prods))
