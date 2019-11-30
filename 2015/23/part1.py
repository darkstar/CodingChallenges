from collections import defaultdict

program = []

def run(prog):
    pc = 0
    regs = { "a": 0, "b": 0 }
    while True:
        if pc < 0 or pc >= len(prog):
            print("Program terminated, a={}, b={}".format(regs["a"], regs["b"]))
            exit(0)
        insn = prog[pc][0]
        args = prog[pc][1]
        if insn == "hlf":
            regs[args[0]] //= 2;
            pc = pc + 1
        if insn == "tpl":
            regs[args[0]] *= 3;
            pc = pc + 1
        if insn == "inc":
            regs[args[0]] += 1
            pc = pc + 1
        if insn == "jmp":
            pc = pc + int(args[0])
        if insn == "jie":
            if regs[args[0]] % 2 == 0:
                pc = pc + int(args[1])
            else:
                pc = pc + 1
        if insn == "jio":
            if regs[args[0]] == 1:
                pc = pc + int(args[1])
            else:
                pc = pc + 1

with open('input.txt', mode='r') as f:
    programcode = f.readlines()
    for l in programcode:
        mnem = l[:3]
        args = l[4:].strip().split(", ")

        insn = (mnem, args)

        program.append(insn)

run(program)

