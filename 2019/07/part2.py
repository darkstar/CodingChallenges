import itertools
import asyncio

# enable this for somme debugging output
debug = False

def dprint(s):
    global debug

    if debug == True:
        print(s)

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
async def run(program, iq, oq, progid):
    pc = 0

    while pc < len(program):
        op = program[pc]
        if opcode(op) == 99:
            # exit
            pc += 1
            dprint("TASK {}: exiting".format(progid))
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
            dprint("TASK {}: waiting for input".format(progid))
            val = await iq.get()
            dprint("TASK {}: received input {}".format(progid, val))
            p1 = program[pc+1]
            program[p1] = val
            pc += 2
            continue
        if opcode(op) == 4:
            # output
            p1 = getparam(op, 1, program[pc+1], program)
            val = p1
            dprint("TASK {}: waiting to write output {}".format(progid, val))
            await oq.put(val)
            dprint("TASK {}: wrote output, continuing...".format(progid))
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

async def runmodel(program, perm):
    tasks = []
    queues = []

    for q in range(5):
        queues.append(asyncio.Queue(1))
    for t in range(5):
        # insert the first value into the queue
        await queues[t].put(perm[t])
        task = asyncio.create_task(run(program.copy(), queues[t], queues[ (t + 1) % 5], chr(ord('A') + t)))
        tasks.append(task)
    # insert the start value into the first queue
    await queues[0].put(0)
    # now the simulation is running
    await asyncio.gather(*tasks)
    # grab the final result from the output queue
    val = await queues[0].get()

    return val
    

async def main():
    perms = list(itertools.permutations([5, 6, 7, 8, 9]))

    with open("input.txt", mode="r") as f:
        program = list(map(lambda x: int(x), f.readline().split(",")))

    #testprogram1 = "3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5"
    #testprogram2 = "3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1," + 
    #               "53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10"
    #program = list(map(lambda x: int(x), testprogram2.split(",")))

    result = 0

    for x in perms:
        val = await runmodel(program, x)
        if (val > result): result = val

    print("result={}".format(result))

asyncio.run(main())
