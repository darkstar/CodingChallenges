
def run(program):
    pc = 0

    while pc < len(program):
        op = program[pc]
        if op == 99:
            # exit
            pc += 1
            return
        if op == 1:
            # Add
            p1 = program[pc+1]
            p2 = program[pc+2]
            p3 = program[pc+3]
            program[p3] = program[p1] + program[p2]
            pc += 4
            continue
        if op == 2:
            # multiply
            p1 = program[pc+1]
            p2 = program[pc+2]
            p3 = program[pc+3]
            program[p3] = program[p1] * program[p2]
            pc += 4
            continue
        print("Illegal opcode {}".format(op))
        exit(1)
    print("Program ran out of bounds")
    exit(1)

with open("input.txt", mode="r") as f:
    program = list(map(lambda x: int(x), f.readline().split(",")))
    # patch the program
    program[1] = 12
    program[2] = 2
    run(program)

    print(program[0])
