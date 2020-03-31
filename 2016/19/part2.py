import re

with open("input.txt") as f:
    elves = int(f.readlines()[0].strip())

#elves = 5

ring = [ { "id": x + 1, "next": None, "prev": None } for x in range(elves) ]

# link elements
for i in range(elves):
    ring[i]["next"] = ring[(i + 1) % elves]
    ring[i]["prev"] = ring[(i - 1) % elves]

start = ring[0]
mid = ring[elves // 2]

#print( [ i["id"] for i in ring ] )

# let the games begin (until all but one elf are out)
for i in range(elves - 1):
    # delete the elf opposite us
    mid["prev"]["next"] = mid["next"]
    mid["next"]["prev"] = mid["prev"]
    mid = mid["next"]

    # odd number of elves remaining? if yes then midpoint changes one further
    if (elves - i) % 2 == 1:
        mid = mid["next"]

    # go to next elf
    start = start["next"]

print(start["id"])
