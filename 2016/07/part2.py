import regex as re

result = 0

def transpose(aba):
    return "{}{}{}".format(aba[1],aba[0],aba[1])

with open("input.txt", mode="r") as f:
    lines = f.readlines()

for addr in lines:
    addr = addr.strip()
    # first, find all strings within brackets
    inner = []
    m = re.findall(r"\[[^\]]*\]", addr)
    for x in m:
        inner.append(x.strip("[]"))
    # then find the outer strings
    outer = re.sub(r"\[[^\]]*\]", "|", addr).split("|")
    # now find all ABAs in the outer strings
    outeraba = []
    for o in outer:
        for c in range(0, len(o) - 2):
            if o[c] == o[c+2] and o[c] != o[c+1]:
                outeraba.append("{}{}{}".format(o[c],o[c+1],o[c+2]))
    # build target list of MAMs
    searchbab = list(map(transpose, outeraba))
    valid = False
    for i in inner:
        for s in searchbab:
            if s in i:
                valid = True
    if valid:
        result += 1

print(result)
