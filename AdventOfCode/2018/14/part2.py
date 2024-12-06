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
    target = list(map(int, list(f.readline().strip())))

recipes = [3, 7]
pos = (0, 1)

tlen = len(target)

while True:
    # see if we're at the end. String grows a maximum of 2 chars per iteration
    c1 = recipes[-tlen:]
    c2 = recipes[-tlen-1:-1]
    if c1 == target:
        print(len(recipes)-tlen)
        break
    if c2 == target:
        print(len(recipes)-tlen-1)
        break

    # create new recipes
    newsum = recipes[pos[0]] + recipes[pos[1]]
    # new sum can only be between 0 and 18
    if newsum > 9:
        recipes += [ 1 ]
    recipes += [ newsum % 10 ]
    # move the elves
    pos = ( (pos[0] + recipes[pos[0]] + 1) % len(recipes),
           (pos[1] + recipes[pos[1]] + 1) % len(recipes))

