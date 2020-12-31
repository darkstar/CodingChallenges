with open("input.txt", mode="r") as f:
    seats = [ int("".join([ "1" if c in "BR" else "0" for c in x.strip() ]), 2) for x in f.readlines() ]

for x in range(1, max(seats) - 1):
    if x not in seats and x-1 in seats and x+1 in seats:
        print(x)

