import re

regex = re.compile(r"^(?P<prefix>\S+\s\S+) bags? contain (no other bags|(?P<others>(\d+\s\S+\s\S+ bags?(, )?)+)).$")
regex2 = re.compile(r"(?P<num>\d+)\s+(?P<prefix>\S+\s\S+) bags?")

allbags = {}

with open("input.txt", mode="r") as f:
    while True:
        l = f.readline().strip()
        if len(l) == 0:
            break
        m = regex.match(l)
        if m:
            if m.group("others"):
                contents = { k : int(v) for (v, k) in regex2.findall(m.group("others"))}
            else:
                contents = {}
            bag = { "prefix": m.group("prefix"), "contents": contents, "containedin": [] }
            allbags[m.group("prefix")] = bag
        else:
            print("No Match: {}".format(l))
            exit(1)

# build reverse mapping for "contained in" relation
for k, v in allbags.items():
    if v["contents"]:
        for c in v["contents"]:
            allbags[c]["containedin"].append(k)

result = set(allbags["shiny gold"]["containedin"])

while True:
    newset = set()
    for bag in result:
        for ibag in allbags[bag]["containedin"]:
            # ignore shiny gold bags
            if ibag == "shiny gold":
                continue
            if ibag not in result:
                newset.add(ibag)
    if len(newset) == 0:
        break
    result.update(newset)

print(len(result))
