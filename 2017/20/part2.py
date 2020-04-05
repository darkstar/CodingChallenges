import re

def dist(p):
    return abs(p[0]) + abs(p[1]) + abs(p[2])

def step(x):
    x["v"][0] += x["a"][0]
    x["v"][1] += x["a"][1]
    x["v"][2] += x["a"][2]
    x["p"][0] += x["v"][0]
    x["p"][1] += x["v"][1]
    x["p"][2] += x["v"][2]

regex = re.compile(r'p=<([- \d]+),([- \d]+),([- \d]+)>, v=<([- \d]+),([- \d]+),([- \d]+)>, a=<([- \d]+),([- \d]+),([- \d]+)>')

particles = []

with open("input.txt") as f:
    num = 0
    for l in f.readlines():
        m = regex.match(l)
        p = [ int(m.group(1)), int(m.group(2)), int(m.group(3)) ]
        v = [ int(m.group(4)), int(m.group(5)), int(m.group(6)) ]
        a = [ int(m.group(7)), int(m.group(8)), int(m.group(9)) ]
        particles.append( { "id": num, "p": p, "v": v, "a": a, "out": False } )
        num += 1

remain = len(particles)

for i in range(100):
    for p in particles:
        # skip collided particles
        if p["out"]:
            continue

        step(p)
        # check for collided particles
        for b in particles:
            if p["id"] == b["id"]:# or b["out"]:
                continue
            if p["p"] == b["p"]:
                p["out"] = True
                b["out"] = True

# find remaining particles
remain = list(filter(lambda x: not x["out"], particles))
print(len(remain))
