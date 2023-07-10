
with open("input.txt", mode="r") as f:
    numbers = [ x.strip() for x in f.readlines() if len(x) > 1 ]

print(str(sum(map(lambda x: int(x), numbers)))[:10])

