with open("input.txt", mode="r") as f:
    seats = [ int("".join([ "1" if c in "BR" else "0" for c in x.strip() ]), 2) for x in f.readlines() ]

print(max(seats))
