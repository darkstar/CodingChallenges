import re

analysis = { "children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3, 
             "akitas": 0, "vizslas": 0, "goldfish": 5, "trees": 3, 
             "cars": 2, "perfumes": 1 }

def trymatch(data):
    for x in data:
        if x not in analysis: return False
        if data[x] != analysis[x]: return False
    return True

with open('input.txt', mode='r') as f:
    lines = f.readlines()
    for line in lines:
        m = re.match('Sue (\d+): (.*)', line)
        nr = int(m.groups()[0])
        rest = m.groups()[1]
        data = {}
        for x in rest.split(','):
            m = re.match(' *(.*): *(\d+)', x)
            data[m.groups()[0]] = int(m.groups()[1])

        if trymatch(data):
            print("Match found: Sue {} ({})".format(nr, data))

