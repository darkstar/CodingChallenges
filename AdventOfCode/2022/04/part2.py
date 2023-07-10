def overlaps(a1, b1, a2, b2):
    return (a2 >= a1 and a2 <= b1) or (a1 >= a2 and a1 <= b2)

result = 0

with open("input.txt", mode="r") as f:
    l = [ s.strip().split(",") for s in f.readlines() ]

for x in l:
    elf1 = list(map(int, x[0].split('-')))
    elf2 = list(map(int, x[1].split('-')))
    if overlaps(elf1[0], elf1[1], elf2[0], elf2[1]):
        result += 1

print(result)
