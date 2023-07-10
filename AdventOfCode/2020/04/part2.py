import re

required = [ "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid" ]

with open("input.txt", mode="r") as f:
    persons = f.read().split("\n\n")

r = re.compile("(?P<key>\S+):(?P<val>\S+)")

numvalid = 0

validators = {
  "byr": lambda v: int(v) >= 1920 and int(v) <= 2002,
  "iyr": lambda v: int(v) >= 2010 and int(v) <= 2020,
  "eyr": lambda v: int(v) >= 2020 and int(v) <= 2030,
  "hgt": lambda v: (v[-2:] == "cm" and int(v[:-2]) >= 150 and int(v[:-2]) <= 193) or
                   (v[-2:] == "in" and int(v[:-2]) >= 59 and int(v[:-2]) <= 76),
  "hcl": lambda v: v[0] == "#" and all(map(lambda c: c in "0123456789abcdef", v[1:])),
  "ecl": lambda v: v in [ "amb", "blu", "brn", "gry", "grn", "hzl", "oth" ],
  "pid": lambda v: len(v) == 9 and all(map(lambda c: c in "0123456789", v)),
  "cid": lambda v: True,
}

for p in persons:
    m = r.findall(p)

    keys = [ x for (x, y) in m ]

    validfields = all(map(lambda x: x in keys, required))

    if validfields:
        # validate fields
        if all(map(lambda x: validators[x[0]](x[1]), m)):
            numvalid += 1

print(numvalid)
