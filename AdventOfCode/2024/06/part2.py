dirs = [ (0, -1), (1, 0), (0, 1), (-1, 0) ]

def mapcopy(mapp):
    return [ [x for x in y] for y in mapp ]

def do_run(mapp):
    size = ( len(mapp[0]), len(mapp) )
    pos = (0, 0)
    curr_dir = 0
    history = set()
    
    # find starting position
    for y in range(len(mapp)):
        if "^" in mapp[y]:
            pos = ( mapp[y].index("^"), y )

    # run the guard
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
            # leave if we've been here before (same spot, same direction)
            if (pos[0], pos[1], curr_dir) in history:
                return None
            history.add( (pos[0], pos[1], curr_dir ) )
            pos = nextpos
    # return number of X's if the guard leaves the map
    return sum(map(lambda x: x.count("X"), mapp))

with open("input.txt", mode="r") as f:
    mapp = [ list(l.strip()) for l in f.readlines() ]

size = ( len(mapp[0]), len(mapp) )

results = 0

# brute force solution (runs in about 30s on my laptop; good enough for me :)
for y in range(len(mapp)):
    for x in range(len(mapp[y])):
        # replace empty space with obstacle
        if mapp[y][x] == '.':
            b = mapcopy(mapp)
            b[y][x] = "#"
            result = do_run(b)
            if result is None:
                results += 1

print(results)
