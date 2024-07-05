cards = []
multiplicity = []

with open("input.txt", mode="r") as f:
    for l in f.readlines():
        l = l.strip()
        name, rest = l.split(":")
        name = name.strip()
        winning, have = rest.split("|")
        winning = set(map(int, winning.split()))
        have = set(map(int, have.split()))
        cards.append( (winning, have) )
        multiplicity.append(1)

for i in range(len(cards)):
    c = cards[i]
    wins = len(c[0].intersection(c[1]))
    for x in range(i + 1, i + 1 + wins):
        multiplicity[x] += multiplicity[i] 


result = sum(multiplicity)

print(result)
