with open("input.txt") as f:
    program = list(map(lambda x: x.split(), f.readlines()))

def get(regs, r):
    try:
        return int(r)
    except:
        if not r in regs:
            regs[r] = 0
        return regs[r]

pc = 0
regs = {}
sndfreq = 0

while True:
    if pc < 0 or pc >= len(program):
        break

    insn = program[pc]
    op = insn[0]
    if op == "snd":
        sndfreq = get(regs, insn[1])
    if op == "set":
        regs[insn[1]] = get(regs, insn[2])
    if op == "add":
        regs[insn[1]] = get(regs, insn[1]) + get(regs, insn[2])
    if op == "mul":
        regs[insn[1]] = get(regs, insn[1]) * get(regs, insn[2])
    if op == "mod":
        regs[insn[1]] = get(regs, insn[1]) % get(regs, insn[2])
    if op == "rcv":
        print(sndfreq)
        break
    if op == "jgz":
        if get(regs, insn[1]) > 0:
            pc += get(regs, insn[2])
            continue
    
    pc += 1

