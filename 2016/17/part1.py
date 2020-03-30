import hashlib

#    x=0         x=3
#   #################
#  y#   |   |   |   #
#  0#   |   |   |   #
#   #---#---#---#---#
#   #   |   |   |   #
#   #   |   |   |   #
#   #---#---#---#---#
#   #   |   |   |   #
#   #   |   |   |   #
#   #---#---#---#---#
#  y#   |   |   |   #
#  3#   |   |   |   #
#   #################

with open("input.txt") as f:
    passcode = f.readlines()[0].strip()

#passcode="ihgpwlah"
#passcode="kglvqrro"
#passcode="ulqzkmiv"

def possibleways(x, y, doors):
    res = []
    if y > 0 and doors["U"]:
        res.append("U")
    if y < 3 and doors["D"]:
        res.append("D")
    if x > 0 and doors["L"]:
        res.append("L")
    if x < 3 and doors["R"]:
        res.append("R")

    return res

# a door is open if it's hash 
def evaldoors(cksum):
    return { "U": cksum[0] in "bcdef",
             "D": cksum[1] in "bcdef",
             "L": cksum[2] in "bcdef",
             "R": cksum[3] in "bcdef" }

def goto(x, y, direction):
    if direction == "U": return (x, y - 1)
    if direction == "D": return (x, y + 1)
    if direction == "L": return (x - 1, y)
    if direction == "R": return (x + 1, y)

paths = [ { "x": 0, "y": 0, "path": "" } ]

while True:
    # check if there are any valid paths left
    if len(paths) == 0:
        print("NO MORE PATHS")
        break
    # get current path
    path = paths.pop(0)
    # are we done yet?
    if path["y"] == 3 and path["x"] == 3:
        print("{} ({})".format(len(path["path"]), path["path"]))
        break
    # get door codes
    # print("path: {}".format(path))
    cksum = hashlib.md5((passcode + path["path"]).encode("ascii")).hexdigest()
    # print("cksum: {}".format(cksum))
    doors = evaldoors(cksum)
    nextsteps = possibleways(path["x"], path["y"], doors)
    # print("next: {}".format(nextsteps))
    for s in nextsteps:
        newpos = goto(path["x"], path["y"], s)
        paths.append({ "x": newpos[0], "y": newpos[1], "path": path["path"] + s})

