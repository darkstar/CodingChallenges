import copy

program = []
registers = { 'a': 0, 'b': 0, 'c': 0, 'd': 0, 'pc': 0 }

def getvalue(registers, x):
    try:
        return int(x)
    except:
        return registers[x]

def executestep(program, registers):
    while registers["pc"] < len(program):
        insn = program[registers["pc"]]
        opcode = insn[0]
        if opcode == "cpy":
            src = getvalue(registers, insn[1])
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
            arg = getvalue(registers, insn[1])
            dst = getvalue(registers, insn[2])
            if arg != 0:
                registers["pc"] += dst
            else:
                registers["pc"] += 1
        elif opcode == "tgl":
            arg = getvalue(registers, insn[1])
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
        elif opcode == "out":
            arg = getvalue(registers, insn[1])
            registers["pc"] += 1
            yield arg

with open("input.txt", mode="r") as f:
    lines = f.readlines()
    for l in lines:
        program.append(l.split())

# first, try with numbers up to 200
states = [ { "num": x, "reg": copy.deepcopy(registers), "run": True, "out": -1, "outstream": [] } for x in range(200) ]

# set up starting register values
for s in states:
    s["reg"]["a"] = s["num"]

# OPTIMIZATION: keep the last two register sets stored. The correct program is where
# these alternate between two different numbers, i.e. new-registers == register[-2], but new-registers != registers[-1]
# luckily, using 200 as upper bound is reasonably quick and gives the right answer (at least here it does)
running = len(states)
while running > 1:
    for s in states:
        # skip program if it is not running anymore
        if not s["run"]:
            continue
        newstate = next(executestep(program, s["reg"]))
        s["outstream"].append(newstate)
        if newstate == s["out"]:
            s["run"] = False
            running -= 1
            # print("  {} is out... ({})".format(s["num"], s["outstream"]))
        else:
            s["out"] = newstate

lastprog = list(filter(lambda x: x["run"], states))[0]
#print("Last program running: {}, signal is {}".format(lastprog["num"], lastprog["outstream"]))
print(lastprog["num"])
