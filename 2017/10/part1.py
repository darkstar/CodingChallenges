with open("input.txt") as f:
    steps = list(map(int, f.readline().strip().split(",")))

lst = [ x for x in range(256) ]
pos = 0
skipsize = 0

for s in steps:
    # start swapping from p1 to p2
    p1 = pos
    p2 = pos + s - 1
    while p2 > p1:
        # swap p1 and p2, and move them
        tmp = lst[p1 % len(lst)]
        lst[p1 % len(lst)] = lst[p2 % len(lst)]
        lst[p2 % len(lst)] = tmp
        p1 += 1
        p2 -= 1
    
    pos = (pos + s + skipsize) % len(lst)
    skipsize += 1

print(lst[0] * lst[1])
