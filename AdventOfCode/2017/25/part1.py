import re

with open("input.txt") as f:
    spec = f.readlines()

state = None
steps = None
pos = 0
fsm = {}

# the tape is initially empty (only 1-values are stored)
tape = {}

m = re.match(r'Begin in state (\S+).', spec[0])
curstate = m.group(1)
    
m = re.match(r'Perform a diagnostic checksum after (\d+) steps.', spec[1])
steps = int(m.group(1))

x = 2

while x < len(spec):
    if spec[x].strip() == "":
        x += 1
        continue
    m = re.match(r'In state (\S+):', spec[x])
    if m:
        state = [ m.group(1), None, None ]
        m1 = re.match(r'.*Write the value (\d+).', spec[x + 2])
        m2 = re.match(r'.*Move one slot to the ((left|right)).', spec[x + 3])
        m3 = re.match(r'.*Continue with state (\S+).', spec[x + 4])
        state[1] = ( int(m1.group(1)), 1 if m2.group(1) == "right" else -1, m3.group(1))
        m1 = re.match(r'.*Write the value (\d+).', spec[x + 6])
        m2 = re.match(r'.*Move one slot to the (left|right).', spec[x + 7])
        m3 = re.match(r'.*Continue with state (\S+).', spec[x + 8])
        state[2] = ( int(m1.group(1)), 1 if m2.group(1) == "right" else -1, m3.group(1))
        
        fsm[state[0]] = state

        x += 9 
        continue
    x += 1

for x in range(steps):
    #print("Step {}: Current state is {} ({})".format(x, curstate, fsm[curstate]))
    val = 1 if pos in tape else 0
    newval = fsm[curstate][val + 1][0]
    direction = fsm[curstate][val + 1][1]
    nextstate = fsm[curstate][val + 1][2]
    #print("  value is {}, new value is {}, next state is {}".format(val, newval, nextstate))
    # write new value
    if val == 1 and newval == 0:
        del tape[pos]
    elif val == 0 and newval == 1:
        tape[pos] = 1
    # update state
    curstate = nextstate
    # move
    pos = pos + direction
    #print("  tape is now {}".format(tape))
    #print("  new pos is {}".format(pos))

print(len(tape))

