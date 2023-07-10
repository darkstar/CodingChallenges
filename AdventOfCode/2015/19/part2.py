import re
import random

rules = []
molecule = ""

with open('input.txt', mode='r') as f:
    lines = f.readlines()
    for line in lines:
        m = re.match('(.*) => (.*)', line)
        if m:
            rules.append((m.groups()[0], m.groups()[1]))
        elif m != "":
            molecule = line.rstrip()

nextmol = molecule
step = 0

while nextmol != 'e':
    tmp = nextmol
    for (a, b) in rules:
        if b not in nextmol:
            continue

        nextmol = nextmol.replace(b, a, 1)
        step += 1

    if tmp == nextmol:
        # no replacement done, restart
        target = mol
        steps = 0
        random.shuffle(rules)

print(step)
