import re

rules = []
molecule = ""

def replaceone(mol):
    results = []
    for x in range(len(mol)):
        # find replacement at this point
        for pat in [p for p in rules if mol[x:].startswith(p[0])]:
            # found a possible replacement
            left = mol[:x]
            right = mol[x + len(pat[0]):]
            results.append(left + pat[1] + right)
    return set(results)

with open('input.txt', mode='r') as f:
    lines = f.readlines()
    for line in lines:
        m = re.match('(.*) => (.*)', line)
        if m:
            rules.append((m.groups()[0], m.groups()[1]))
        elif m != "":
            molecule = line.rstrip()

print(len(replaceone(molecule)))

