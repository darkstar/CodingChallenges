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
    if all(map(lambda x: valid(p, x), rules)):
        result += p[len(p)//2]

print(result)
