import re

def calc(x):
    v = re.match(r"mul\((\d+),(\d+)\)", x)
    a = int(v.group(1))
    b = int(v.group(2))
    return a * b

with open("input.txt", mode="r") as f:
    code = "".join([l.strip() for l in f.readlines()])

print(len(code))
code = re.sub(r'don\'t\(\).*?(do\(\)|$)', '', code)
print(len(code))
muls = re.findall(r"mul\(\d{1,3},\d{1,3}\)", code)

prods = list(map(lambda x: calc(x), muls))

print(sum(prods))
