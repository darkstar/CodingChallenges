with open("input.txt") as f:
    memory = list(map(int, f.readline().split()))

# memory = [ 0, 2, 7, 0 ]

states = set([" ".join(map(str, memory))])
cycle = 0

while True:
    # next cycle
    cycle += 1
    # which position to redistribute?
    pos = memory.index(max(memory))
    # distribute:
    blocks = memory[pos]
    memory[pos] = 0
    for x in range(pos + 1, pos + 1 + blocks):
        memory[x % len(memory)] += 1
    # check if the config was already seen
    newstate = " ".join(map(str, memory))
    if newstate in states:
        break
    states.add(newstate)

print(cycle)
