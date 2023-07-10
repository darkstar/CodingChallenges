allvalues = "23456789TJQKA"

def sortkey(c):
    values = { "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14 }
    return values[c] if c in values else int(c)

def flush(cards):
    suits = set(map(lambda x: x[1], cards))
    if len(suits) > 1:
        return None
    # calculate value of the flush
    v = list(map(sortkey, map(lambda x: x[0], cards)))
    v.sort()
    res =0 
    while len(v) > 0:
        res = 20 * res + v[-1]
        v = v[:-1]
    return res

def royalflush(cards):
    suits = set(map(lambda x: x[1], cards))
    if len(suits) > 1:
        return None
    cards = set(map(lambda x: x[0], cards))
    if len(cards) != 5:
        return None
    if len(cards.intersection(set("TJQKA"))) == 5:
        return 1
    return None

def straightflush(cards):
    suits = set(map(lambda x: x[1], cards))
    if len(suits) > 1:
        return None
    cards = list(map(lambda x: x[0], cards))
    cards.sort(key = sortkey)
    if "".join(cards) in allvalues:
        return sortkey(cards[0])
    return None

def fourofakind(cards):
    vals = list(map(lambda x: x[0], cards))
    c = { x: vals.count(x) for x in allvalues }
    m = max(c, key=c.get)
    if c[m] < 4:
        return None
    print(cards, m, c[m])

def threeofakind(cards):
    vals = list(map(lambda x: x[0], cards))
    c = { x: vals.count(x) for x in allvalues }
    m = max(c, key=c.get)
    if c[m] < 3:
        return None
    return sortkey(m)

def straight(cards):
    c = list(map(lambda x: x[0], cards))
    c.sort(key=sortkey)
    c = "".join(c)
    if c in allvalues:
        return sortkey(c[4])
    return None

def twopairs(cards):
    vals = list(map(lambda x: x[0], cards))
    c = { x: vals.count(x) for x in allvalues if vals.count(x) == 2 }
    if len(c) == 2:
        s = [ x for x in c.keys() ]
        s.sort(key=sortkey)
        result = sortkey(s[0]) + sortkey(s[1]) * 20
        return result
    return None

def pair(cards):
    vals = list(map(lambda x: x[0], cards))
    c = { x: vals.count(x) for x in allvalues if vals.count(x) == 2 }
    if len(c) == 1:
        s = [x for x in c.keys()][0]
        return sortkey(s)
    return None

def fullhouse(cards):
    vals = list(map(lambda x: x[0], cards))
    c = { x: vals.count(x) for x in allvalues if vals.count(x)>0 }
    three = [ x for x in c.keys() if c[x] == 3 ]
    if len(three) == 0:
        return None
    two = [ x for x in c.keys() if c[x] == 2 ]
    if len(two) == 0:
        return None
    return 20 * sortkey(three[0]) + sortkey(two[0])

def rubbish(cards):
    vals = list(map(lambda x: sortkey(x[0]), cards))
    vals.sort()
    res = 0 
    while len(vals) > 0:
        res = 20 * res + vals[-1]
        vals = vals[:-1]
    return res

def wins(p1, p2):
    funcs = { "royal flush": royalflush, 
            "straight flush": straightflush,
            "four of a kind": fourofakind, 
            "full house": fullhouse, 
            "flush": flush, 
            "straight": straight, 
            "threeofakind": threeofakind, 
            "twopairs": twopairs, 
            "pair": pair, 
            "rubbish": rubbish }

    for s, f in funcs.items():
        f1 = f(p1)
        f2 = f(p2)
#        if f1 or f2:
#            print(s)
        if f1 and f2:
            return 1 if f1 > f2 else 2
        if f1: 
            return 1
        if f2:
            return 2
    return None

with open("input.txt", mode="r") as f:
    hands = [ x.strip().split(" ") for x in f.readlines() ]

p1wins = 0

for game in hands:
    p1 = game[:5]
    p2 = game[5:]
#    print("{} vs {}: P{} wins".format(p1, p2, wins(p1, p2)))
    if wins(p1, p2) == 1:
        p1wins += 1

print(p1wins)
