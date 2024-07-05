cards = []

with open("input.txt", mode="r") as f:
    for l in f.readlines():
        l = l.strip()
        name, rest = l.split(":")
        name = name.strip()
        winning, have = rest.split("|")
        winning = set(map(int, winning.split()))
        have = set(map(int, have.split()))
        cards.append( (winning, have) )

result = 0
for c in cards:
    wins = c[0].intersection(c[1])
    if len(wins) > 0:
        result += 2**(len(wins) - 1)

print(result)
