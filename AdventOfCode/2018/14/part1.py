def draw(rec, pos):
    for i in range(len(rec)):
        if pos[0] == i:
            print("({}) ".format(rec[i]), end="")
        elif pos[1] == i:
            print("[{}] ".format(rec[i]), end="")
        else:
            print("{} ".format(rec[i]), end="")
    print("")

with open("input.txt", mode="r") as f:
    target = int(f.readline().strip())

recipes = [3, 7]
pos = (0, 1)

while len(recipes) <= target + 10:
    # create new recipes
    newsum = recipes[pos[0]] + recipes[pos[1]]
    # new sum can only be between 0 and 18
    if newsum > 9:
        recipes += [ 1, newsum % 10 ]
    else:
        recipes += [ newsum ]
    # move the elves
    pos = ( (pos[0] + recipes[pos[0]] + 1) % len(recipes),
           (pos[1] + recipes[pos[1]] + 1) % len(recipes))

print("".join(map(str,recipes[target:target+10])))
