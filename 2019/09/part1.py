
# returns the parameter mode for the parameter with number pnum
def pmode(op, pnum):
    parammask = 10 ** (pnum - 1)
    pmode = ((op // 100) // parammask) % 10
    return pmode

# returns the raw opcode
def opcode(op):
    return op % 100

def getparam(pc, pnum, memory, rbase):
    parammode = pmode(memory[pc], pnum)
    pval = memory[pc + pnum]
    if parammode == 0: # POSITION mode
        return memory[pval]
    if parammode == 1: # INDIRECT mode
        return pval
    if parammode == 2: # RELATIVE mode
        return memory[rbase + pval]
    print("Invalid parameter mode {}".format(parammode))
    exit(1)

def setparam(pc, pnum, memory, rbase, value):
    parammode = pmode(memory[pc], pnum)
    pval = memory[pc + pnum]
    if parammode == 0: # POSITION mode
        memory[pval] = value
    elif parammode == 1: # INDIRECT mode
        print("Mode 1 invalid for output parameter")
        exit(2)
    elif parammode == 2: # RELATIVE mode
        memory[rbase + pval] = value
    else:
        print("Invalid parameter mode {}".format(parammode))
        exit(1)
    

# istream and ostream are lists with the input values
def run(program, istream, ostream):
    pc = 0
    rbase = 0

    while True:
        op = program[pc]
        if opcode(op) == 99:
            # exit
            pc += 1
            return
        if opcode(op) == 1:
            # Add
            p1 = getparam(pc, 1, program, rbase)
            p2 = getparam(pc, 2, program, rbase)
            setparam(pc, 3, program, rbase, p1 + p2)
            pc += 4
            continue
        if opcode(op) == 2:
            # multiply
            p1 = getparam(pc, 1, program, rbase)
            p2 = getparam(pc, 2, program, rbase)
            setparam(pc, 3, program, rbase, p1 * p2)
            pc += 4
            continue
        if opcode(op) == 3:
            # input
            val = istream.pop(0)
            setparam(pc, 1, program, rbase, val)
            pc += 2
            continue
        if opcode(op) == 4:
            # output
            p1 = getparam(pc, 1, program, rbase)
            val = p1
            ostream.append(val)
            pc += 2
            continue
        if opcode(op) == 5:
            # jump-if-true
            p1 = getparam(pc, 1, program, rbase)
            p2 = getparam(pc, 2, program, rbase)
            if p1 != 0:
                pc = p2
            else:
                pc += 3
            continue
        if opcode(op) == 6:
            # jump-if-false
            p1 = getparam(pc, 1, program, rbase)
            p2 = getparam(pc, 2, program, rbase)
            if p1 == 0:
                pc = p2
            else:
                pc += 3
            continue
        if opcode(op) == 7:
            # less-than
            p1 = getparam(pc, 1, program, rbase)
            p2 = getparam(pc, 2, program, rbase)
            setparam(pc, 3, program, rbase, 1 if p1 < p2 else 0)
            pc += 4
            continue
        if opcode(op) == 8:
            # equals
            p1 = getparam(pc, 1, program, rbase)
            p2 = getparam(pc, 2, program, rbase)
            setparam(pc, 3, program, rbase, 1 if p1 == p2 else 0)
            pc += 4
            continue
        if opcode(op) == 9:
            # adjust relative base
            p1 = getparam(pc, 1, program, rbase)
            rbase += p1
            pc += 2
            continue
        print("Illegal opcode {}".format(op))
        exit(1)

out = []
with open("input.txt", mode="r") as f:
    code = f.readline()
    #code = "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99" # test program
    program = list(map(lambda x: int(x), code.split(",")))
    padding = [ 0 ] * (65536 - len(program))
    program = program + padding
    run(program, [ 1 ], out)

print(out)

