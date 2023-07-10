import re

required = [ "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid" ]

with open("input.txt", mode="r") as f:
    persons = f.read().split("\n\n")

r = re.compile("(?P<key>\S+):(?P<val>\S+)")

valid = 0

for p in persons:
    m = r.findall(p)

    keys = [ x for (x, y) in m ]

    validpassport = all(map(lambda x: x in keys, required))

    if validpassport:
        valid += 1

print(valid)
