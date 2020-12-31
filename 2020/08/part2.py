import re

regex = re.compile(r"^(?P<op>\S+)\s+(?P<arg>[+-]\d+)$")

with open("input.txt", mode="r") as f:
    code = list(map(lambda x: (x.group("op"), int(x.group("arg"))), [regex.match(x) for x in f.readlines()]))

# returns False if the program ends in an endless loop, otherwise returns a
def runprogram(code):
    state = { "a": 0, "pc": 0 }
    visited = set()
    
    while True:
        if state["pc"] == len(code):
            # found the program that terminates
            return state["a"]
        if state["pc"] in visited:
            # endless loop, return false
            return False
        insn = code[state["pc"]]
        visited.add(state["pc"])
        if insn[0] == "nop":
            # NOP
            state["pc"] += 1
            continue
        if insn[0] == "acc":
            # modify accumulator
            state["a"] += insn[1]
            state["pc"] += 1
            continue
        if insn[0] == "jmp":
            # Jump
            state["pc"] += insn[1]
            continue
        print("Illegal instruction {} at pc={}".format(insn[0], state["pc"]))

# Brute force: just generate all possible corrupted programs
# and run them all

programs = []

for i in range(len(code)):
    if code[i][0] == "nop":
        newprogram = code.copy()
        newprogram[i] = ("jmp", code[i][1])
        programs.append(newprogram)
    if code[i][0] == "jmp":
        newprogram = code.copy()
        newprogram[i] = ("nop", code[i][1])
        programs.append(newprogram)

results = list(filter(lambda x: x, map(runprogram, programs)))

print(results[0])
