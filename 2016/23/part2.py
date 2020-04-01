program = []
registers = { 'a': 0, 'b': 0, 'c': 0, 'd': 0, 'pc': 0 }

def getvalue(x):
    global registers
    try:
        return int(x)
    except:
        return registers[x]

def executestep(program):
    global registers
    insn = program[registers["pc"]]
    opcode = insn[0]
    #print("{} : {}".format(registers["pc"], insn))
    if opcode == "nop":
        registers["pc"] += 1
    elif opcode == "add":
        dst = insn[1]
        src = getvalue(insn[2])
        registers[dst] += src
        registers["pc"] += 1
    elif opcode == "mul":
        dst = insn[1]
        src = insn[2]
        registers[dst] = registers[dst] * registers[src]
        registers["pc"] += 1
    elif opcode == "cpy":
        src = getvalue(insn[1])
        dst = insn[2]
        # skip invalid instructions
        if dst in ['a', 'b', 'c', 'd']:
            registers[dst] = src
        registers["pc"] += 1
    elif opcode == "inc":
        reg = insn[1]
        # skip invalid instructions
        if reg in ['a', 'b', 'c', 'd']:
            registers[reg] += 1
        registers["pc"] += 1
    elif opcode == "dec":
        reg = insn[1]
        # skip invalid instructions
        if reg in ['a', 'b', 'c', 'd']:
            registers[reg] -= 1
        registers["pc"] += 1
    elif opcode == "jnz":
        arg = getvalue(insn[1])
        dst = getvalue(insn[2])
        if arg != 0:
            registers["pc"] += dst
        else:
            registers["pc"] += 1
    elif opcode == "tgl":
        arg = getvalue(insn[1])
        dest = registers["pc"] + arg
        # see if te target is within program space
        if dest >= 0 and dest < len(program):
            #print("Toggling {} at {}".format(program[dest][0], registers["pc"]))
            if program[dest][0] in ["tgl", "dec"]:
                program[dest][0] = "inc"
            elif program[dest][0] == "inc":
                program[dest][0] = "dec"
            elif program[dest][0] in ["cpy"]:
                program[dest][0] = "jnz"
            elif program[dest][0] == "jnz":
                program[dest][0] = "cpy"
            else:
                print("hmmm...")
                exit(1)
        registers["pc"] += 1

def run(prog):
    global registers
    while registers["pc"] < len(prog):
        executestep(prog)

with open("input.txt", mode="r") as f:
    lines = f.readlines()
    for l in lines:
        program.append(l.split())

# the input
registers['a'] = 12
registers['pc'] = 0

# patch program to optimize addition
#program[5] = [ "add", "a", "c" ]
#program[6] = [ "cpy", "0", "c" ]
#program[7] = [ "nop" ]

# patch program to optimize multiplication
# note: this will only work with the given input,
# other programs/puzzle inputs might need tweaking!
# I didn't want to build a full assembly optimizer :)
program[2] = [ "mul", "a", "b" ]
program[3] = [ "cpy", "0", "c" ]
program[4] = [ "cpy", "0", "d" ]
program[5] = [ "nop" ]
program[6] = [ "nop" ]
program[7] = [ "nop" ]
program[8] = [ "nop" ]
program[9] = [ "nop" ]
run(program)

print(registers['a'])
