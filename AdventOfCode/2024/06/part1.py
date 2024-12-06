with open("input.txt", mode="r") as f:
    mapp = [ list(l.strip()) for l in f.readlines() ]

size = ( len(mapp[0]), len(mapp) )

pos = (0, 0)
dirs = [ (0, -1), (1, 0), (0, 1), (-1, 0) ]
curr_dir = 0

# find starting position
for y in range(len(mapp)):
    if "^" in mapp[y]:
        pos = ( mapp[y].index("^"), y )

while True:
    # get coordinates of the next square
    nextpos = ( pos[0] + dirs[curr_dir][0], pos[1] + dirs[curr_dir][1] )
    # check if we're out of bounds
    if nextpos[0] < 0 or nextpos[0] >= size[0] or nextpos[1] < 0 or nextpos[1] >= size[1]:
        break
    # get the content of the next field
    field = mapp[nextpos[1]][nextpos[0]]

    if field == "#":
        # turn right if blocked
        curr_dir = (curr_dir + 1) % 4
    else:
        # mark current square visited and move on
        mapp[nextpos[1]][nextpos[0]] = "X"
        pos = nextpos

result = sum(map(lambda x: x.count("X"), mapp))
print(result)
