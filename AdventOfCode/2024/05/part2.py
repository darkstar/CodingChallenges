rules = []
pages = []

def valid(pages, rule):
    a, b = rule
    # if both are in the set of pages,
    # then see if they obey the rule
    if a in pages and b in pages:
        return pages.index(a) < pages.index(b)
    # if not both are in, then the rule is satisfied
    return True

with open("input.txt", mode="r") as f:
    # read the rules
    while True:
        l = f.readline().strip()
        if len(l) == 0:
            break
        a, b = l.split("|")
        rules.append( (int(a), int(b)) )
    # read the pages
    while True:
        l = f.readline()
        if len(l) == 0:
            break
        pages.append(list(map(int, l.strip().split(","))))

result = 0
for p in pages:
    # ignore entries that are already correct
    if all(map(lambda x: valid(p, x), rules)):
        continue

    # fix the unsorted ones with only the subset of rules that are relevant
    subrules = [ x for x in rules if x[0] in p and x[1] in p ]

    # swap until we don't need to swap anymore
    while True:
        swaps = 0
        for x in subrules:
            i1 = p.index(x[0])
            i2 = p.index(x[1])
            # swap if they are the wrong way around
            if i2 < i1:
                temp = p[i1]
                p[i1] = p[i2]
                p[i2] = temp
                swaps += 1
        # finished if we don't have to do any more swaps
        if swaps == 0:
            break
    # the middle item should now be correct
    result += p[len(p)//2]

print(result)
