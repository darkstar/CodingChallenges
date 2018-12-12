import re

initialstate = ""
rules = {}

with open('input.txt', mode='r') as f:
    lines = f.readlines()
    for line in lines:
        m = re.match('initial state: (.*)', line)
        if m: initialstate = m.groups()[0]

        m = re.match('(.....) => (.)', line)
        if m:
            rules[m.groups()[0].strip()] = m.groups()[1].strip()

print("Initial: ", initialstate)
print(rules)
