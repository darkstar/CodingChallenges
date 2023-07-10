import re

initialstate = ""
rules = {}

# centered around 0
state = "." * 500

def dostep():
    newstate = ['.' for x in range(500)]
    for x in range(2, 500 - 2):
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

state = ['.' for x in range(500)]
for x in range(len(initialstate)):
    state[x + 100] = initialstate[x]

state = "".join(state)

#print("i :", state[90:250])
for step in range(20):
    state = dostep()
#    print(step + 1, ":", state[90:250])

result = 0
for x in range(500):
    if state[x] == '#': result += x - 100

print(result)
