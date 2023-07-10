import asyncio

with open("input.txt") as f:
    program = list(map(lambda x: x.split(), f.readlines()))

#program = [
#    ["snd", "1"],
#    ["snd", "2"],
#    ["snd", "p"],
#    ["rcv", "a"],
#    ["rcv", "b"],
#    ["rcv", "c"],
#    ["rcv", "d"]
#]

def get(regs, r):
    try:
        return int(r)
    except:
        if not r in regs:
            regs[r] = 0
        return regs[r]

# OPTIMIZE: This is not necessarily correct, but it works
# we need to check that BOTH programs deadlock simultaneously
async def run(program, pid, iq, oq, deadlockevent, result):
    pc = 0
    regs = { "p": pid }
    sndfreq = 0

    while True:
        if pc < 0 or pc >= len(program):
            break

        insn = program[pc]
        op = insn[0]
        if op == "snd":
#            print("program {} sending {}".format(pid, get(regs, insn[1])))
            result[pid] = result[pid] + 1
            await oq.put(get(regs, insn[1]))
        if op == "set":
            regs[insn[1]] = get(regs, insn[2])
        if op == "add":
            regs[insn[1]] = get(regs, insn[1]) + get(regs, insn[2])
        if op == "mul":
            regs[insn[1]] = get(regs, insn[1]) * get(regs, insn[2])
        if op == "mod":
            regs[insn[1]] = get(regs, insn[1]) % get(regs, insn[2])
        if op == "rcv":
            if iq.empty() and oq.empty():
#                print("program {} deadlocked".format(pid))
                deadlockevent.set()
                return
            regs[insn[1]] = await iq.get()
#            print("program {} received {}".format(pid, regs[insn[1]]))
        if op == "jgz":
            if get(regs, insn[1]) > 0:
                pc += get(regs, insn[2])
                continue
    
        pc += 1

async def main():
    q1 = asyncio.Queue()
    q2 = asyncio.Queue()
    deadlock = asyncio.Event()
    result = { 0: 0, 1: 0 }
    
    t1 = asyncio.create_task(run(program, 0, q1, q2, deadlock, result))
    t2 = asyncio.create_task(run(program, 1, q2, q1, deadlock, result))

    await deadlock.wait()
    #await asyncio.gather(t1, t2)
    print(result[1])

asyncio.run(main())

