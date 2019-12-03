delta = { "U": (0, 1), "D": (0, -1), "R": (1, 0), "L": (-1, 0) }

segdirs = { "U": "|", "D": "|", "L": "-", "R": "-" }

crossings = []

def pointonsegment(p, seg):
    if seg[0] == "|":
        # vertical segment
        sy1 = min(seg[1][1], seg[2][1])
        sy2 = max(seg[1][1], seg[2][1])
        return p[0] == seg[1][0] and p[1] >= sy1 and p[1] <= sy2
    if seg[0] == "-":
        # horizontal segment
        sx1 = min(seg[1][0], seg[2][0])
        sx2 = max(seg[1][0], seg[2][0])
        return p[0] >= sx1 and p[0] <= sx2 and p[1] == seg[1][1]

def tracepath(s):
    pos = (0, 0)
    path = []
    for step in s.split(","):
       direction = step[0]
       count = int(step[1:])
       segstart = pos
       segend = (pos[0] + count * delta[direction][0],
                 pos[1] + count * delta[direction][1])
       path.append( (segdirs[direction], segstart, segend) )
       pos = segend
    return path

def pointonpath(p, path):
    for x in path:
        if pointonsegment(p, x): return True
    return False

def checkpath(s, otherpath):
    global crossings
    fullpath = [ (0, 0) ]

    pos = (0, 0)
    for step in s.split(","):
       direction = step[0]
       count = int(step[1:])
       for x in range(count):
           pos = ( pos[0] + delta[direction][0], pos[1] + delta[direction][1] )
           if otherpath is None:
               fullpath.append(pos)
           elif pointonpath(pos, otherpath):
               dist = abs(pos[0]) + abs(pos[1])
               # print("Possible hit: {}, dist = {}".format(pos, dist))
               crossings.append(pos)
    if otherpath is None:
        return fullpath

print("please wait, this will take a moment...")

with open("input.txt", mode="r") as f:
    lines = f.readlines()
    p1 = tracepath(lines[0].strip())
    p2 = checkpath(lines[1].strip(), p1)

pl1 = checkpath(lines[0].strip(), None) # only build the path map
pl2 = checkpath(lines[1].strip(), None)

result = 999999

for i in crossings:
    idx1 = pl1.index(i)
    idx2 = pl2.index(i)
    if idx1 + idx2 < result:
        result = idx1 + idx2

print(result)
