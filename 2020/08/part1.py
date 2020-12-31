import re

regex = re.compile(r"^(?P<op>\S+)\s+(?P<arg>[+-]\d+)$")

with open("input.txt", mode="r") as f:
    code = list(map(lambda x: (x.group("op"), int(x.group("arg"))), [regex.match(x) for x in f.readlines()]))

state = { "a": 0, "pc": 0 }
visited = set()

while True:
    if state["pc"] in visited:
        print("Infinite Loop detected, last value of a:")
        print(state["a"])
        break
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

