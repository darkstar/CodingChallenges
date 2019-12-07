import itertools

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
        if opcode(op) == 5:
            # jump-if-true
            p1 = getparam(op, 1, program[pc+1], program)
            p2 = getparam(op, 2, program[pc+2], program)
            if p1 != 0:
                pc = p2
            else:
                pc += 3
            continue
        if opcode(op) == 6:
            # jump-if-false
            p1 = getparam(op, 1, program[pc+1], program)
            p2 = getparam(op, 2, program[pc+2], program)
            if p1 == 0:
                pc = p2
            else:
                pc += 3
            continue
        if opcode(op) == 7:
            # less-than
            p1 = getparam(op, 1, program[pc+1], program)
            p2 = getparam(op, 2, program[pc+2], program)
            p3 = program[pc+3]
            program[p3] = 1 if p1 < p2 else 0
            pc += 4
            continue
        if opcode(op) == 8:
            # equals
            p1 = getparam(op, 1, program[pc+1], program)
            p2 = getparam(op, 2, program[pc+2], program)
            p3 = program[pc+3]
            program[p3] = 1 if p1 == p2 else 0
            pc += 4
            continue
        print("Illegal opcode {}".format(op))
        exit(1)
    print("Program ran out of bounds")
    exit(1)

perms = list(itertools.permutations([0, 1, 2, 3, 4]))

with open("input.txt", mode="r") as f:
    program = list(map(lambda x: int(x), f.readline().split(",")))

#testprogram1 = "3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0"
#testprogram2 = "3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0"
#testprogram3 = "3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0"
#program = list(map(lambda x: int(x), testprogram3.split(",")))

result = 0

for x in perms:
    val = 0
    for amp in range(5):
        p = program.copy()
        i = [ x[amp], val ]
        o = []
        run(p, i, o)
        val = o[0]
    if (val > result): result = val

print(result)
