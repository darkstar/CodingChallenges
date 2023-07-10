import re

initialstate = ""
rules = {}

# centered around 0
state = "." * 5000

def docount():
    result = 0
    for x in range(5000):
        if state[x] == '#': result += x - 100
    return result

def dostep():
    newstate = ['.' for x in range(5000)]
    for x in range(2, 5000 - 2):
        neigh = "".join(state[x - 2:x - 2 + 5])
        newstate[x] = rules[neigh]

    return "".join(newstate)

with open('input.txt', mode='r') as f:
    lines = f.readlines()
    for line in lines:
        m = re.match('initial state: (.*)', line)
        if m: initialstate = m.groups()[0]

        m = re.match('(.....) => (.)', line)
        if m:
            rules[m.groups()[0]] = m.groups()[1]

state = ['.' for x in range(5000)]
for x in range(len(initialstate)):
    state[x + 100] = initialstate[x]

state = "".join(state)

# this is specific to my case, no idea if it works in general
# in my case, the result had a constant difference from a certain
# point on
laststeps = [0, 0, 0, 0, 0]

for step in range(1000):
    state = dostep()
    laststeps = laststeps[1:] + [docount()]
    deltas = [laststeps[x + 1] - laststeps[x] for x in range(len(laststeps) - 1)]
    #print(step + 1, ":", laststeps, deltas)

#print("result after 1000 steps: {}, delta = {}"dmt(ount(), deltas[0]))
print("result = {}".format((50000000000 - 1000) * deltas[0] + docount()))

