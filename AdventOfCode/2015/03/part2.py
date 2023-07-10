visited = {}

pos = [(0,0), (0,0)]
who = 0

def next(pos, ch):
    if ch == '^': return (pos[0], pos[1]+1)
    if ch == 'v': return (pos[0], pos[1]-1)
    if ch == '<': return (pos[0]-1, pos[1])
    if ch == '>': return (pos[0]+1, pos[1])

    return (0,0)

def visit(loc):
    global visited

    if loc in visited:
        visited[loc] += 1
    else:
        visited[loc] = 1

with open('input.txt', mode='r') as f:
    instr = f.readlines()[0].rstrip()

    visit((0,0))

    for i in instr:
        pos[who] = next(pos[who], i)
        visit(pos[who])
        who = 1 - who

print(len(visited))

