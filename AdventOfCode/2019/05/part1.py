
# returns the parameter mode for the parameter with number pnum
def pmode(op, pnum):
    parammask = 10 ** (pnum - 1)
    pmode = ((op // 100) // parammask) % 10
    return pmode

# returns the raw opcode
def opcode(op):
    return op % 100

def getparam(op, pnum, pval, memory):
    parammode = pmode(op, pnum)
    if parammode == 0:
        return memory[pval]
    if parammode == 1:
        return pval
    print("Invalid parameter mode {}".format(parammode))
    exit(1)

# istream and ostream are lists with the input values
def run(program, istream, ostream):
    pc = 0

    while pc < len(program):
        op = program[pc]
        if opcode(op) == 99:
            # exit
            pc += 1
            return
        if opcode(op) == 1:
            # Add
            p1 = getparam(op, 1, program[pc+1], program)
            p2 = getparam(op, 2, program[pc+2], program)
            p3 = program[pc+3]
            program[p3] = p1 + p2
            pc += 4
            continue
        if opcode(op) == 2:
            # multiply
            p1 = getparam(op, 1, program[pc+1], program)
            p2 = getparam(op, 2, program[pc+2], program)
            p3 = program[pc+3]
            program[p3] = p1 * p2
            pc += 4
            continue
        if opcode(op) == 3:
            # input
            val = istream.pop(0)
            p1 = program[pc+1]
            program[p1] = val
            pc += 2
            continue
        if opcode(op) == 4:
            # output
            p1 = getparam(op, 1, program[pc+1], program)
            val = p1
            ostream.append(val)
            pc += 2
            continue
        print("Illegal opcode {}".format(op))
        exit(1)
    print("Program ran out of bounds")
    exit(1)

out = []
with open("input.txt", mode="r") as f:
    program = list(map(lambda x: int(x), f.readline().split(",")))
    run(program, [1], out)

print(out)

