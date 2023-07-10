def variants2(x):
    # input: a string of the form "ab/cd"
    # output: a list of all rotations and mirror images
    # including the original (only different ones)
    a = x[0]
    b = x[1]
    c = x[3]
    d = x[4]
    results = list(map(lambda f: "{}{}/{}{}".format(*f),
        [ (a, b, c, d), (b, d, a, c), (c, a, d, b), (d, c, b, a),
          (b, a, d, c), (d, b, c, a), (a, c, b, d), (c, d, a, b) ]))
    return list(set(results))

def variants3(x):
    # input: a string of the form "abc/def/ghi"
    # output: all variations of that string
    # (only different ones)
    (a, b, c) = (x[0], x[1], x[2])
    (d, e, f) = (x[4], x[5], x[6])
    (g, h, i) = (x[8], x[9], x[10])
    results = list(map(lambda f: "{}{}{}/{}{}{}/{}{}{}".format(*f),
        [ (a, b, c, d, e, f, g, h, i), (c, f, i, b, e, h, a, d, g), (g, d, a, h, e, b, i, f, c), (i, h, g, f, e, d, c, b, a),
          (c, b, a, f, e, d, i, h, g), (a, d, g, b, e, h, c, f, i), (i, f, c, h, e, b, g, d, a), (g, h, i, d, e, f, a, b, c)]))
    return list(set(results))

def variants(x):
    if len(x) == 5:
        return variants2(x)
    else:
        return variants3(x)

def blk2str(b):
    return "/".join([ "".join(x) for x in b ])

def str2blk(s):
    return s.split("/")

with open("input.txt") as f:
    rules = list(map(lambda x: x.strip().split(" => "),  f.readlines()))

rulebook = {}

# prepare the rules for easier matching
for r in rules:
    for v in variants(r[0]):
        rulebook[v] = r[1]

# the start program
program = [ ".#.", "..#", "###" ]

for step in range(18):
    # determine block size
    if len(program) % 2 == 0:
        blocksize = 2
    else:
        blocksize = 3

    newprogram = []
    # split program into row slices
    for y in range(len(program) // blocksize):
        rows = program[blocksize * y: blocksize * (y + 1)]
        # split each row into blocks
        blocks = []
        for x in range(len(program) // blocksize):
            blk = [ f[blocksize * x:blocksize * (x+1)] for f in rows ]
            blocks.append(blk)
        # convert blocks to strings
        blocks = list(map(blk2str, blocks))

        # translate via rulebook
        newblocks = list(map(lambda x: str2blk(rulebook[x]), blocks))

        # slice together the new program
        newrows = []
        for x in range(len(newblocks[0])):
            newrows.append( "".join(list(map(lambda f: f[x], newblocks))) )
    
        newprogram += newrows

    # update our program to the new program
    program = newprogram

print("".join(program).count("#"))
