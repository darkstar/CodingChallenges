import re

analysis = { "children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3, 
             "akitas": 0, "vizslas": 0, "goldfish": 5, "trees": 3, 
             "cars": 2, "perfumes": 1 }
larger = [ "cats", "trees" ] # data must be larger than analysis result
smaller = [ "pomeranians", "goldfish" ] # data needs to be smaller than analysis result

def trymatch(nr, data):
    for x in data:
        if x in larger:
            if data[x] <= analysis[x]: return False
        elif x in smaller:
            if data[x] >= analysis[x]: return False
        else: 
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
            m = re.match('(.*): *(\d+)', x)
            data[(m.groups()[0]).strip()] = int(m.groups()[1])

        if trymatch(nr, data):
            print("Match found: Sue {} ({})".format(nr, data))

