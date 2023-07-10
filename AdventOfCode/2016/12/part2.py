program = []
registers = { 'a': 0, 'b': 0, 'c': 1, 'd': 0, 'pc': 0 }

def getvalue(x):
    global registers
    try:
        return int(x)
    except:
        return registers[x]

def execute(insn):
    global registers
    opcode = insn[0]
    if opcode == "cpy":
        src = getvalue(insn[1])
        dst = insn[2]
        registers[dst] = src
        registers["pc"] += 1
    elif opcode == "inc":
        reg = insn[1]
        registers[reg] += 1
        registers["pc"] += 1
    elif opcode == "dec":
        reg = insn[1]
        registers[reg] -= 1
        registers["pc"] += 1
    elif opcode == "jnz":
        arg = getvalue(insn[1])
        dst = getvalue(insn[2])
        if arg != 0:
            registers["pc"] += dst
        else:
            registers["pc"] += 1

def run(prog):
    global registers
    while registers["pc"] < len(program):
        insn = program[registers["pc"]]
        execute(insn)

with open("input.txt", mode="r") as f:
    lines = f.readlines()
    for l in lines:
        program.append(l.split())

run(program)
print(registers["a"])
