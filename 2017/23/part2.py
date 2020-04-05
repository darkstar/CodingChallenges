with open("input.txt") as f:
    program = list(map(lambda x: x.split(), f.readlines()))

def isPrime(n):
    # Corner cases
    if (n <= 1):
        return False
    if (n <= 3):
        return True

    # This is checked so that we can skip
    # middle five numbers in below loop
    if (n % 2 == 0 or n % 3 == 0):
        return False
    i = 5
    while(i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6
    return True

def get(regs, r):
    try:
        return int(r)
    except:
        if not r in regs:
            regs[r] = 0
        return regs[r]

# I tried to keep this as generic as possible, but
# it might not work for every input if the program
# code is reasonably different

h = 0
start = int(program[0][2]) * int(program[4][2]) - int(program[5][2])
end = start - int(program[7][2])
delta = - int(program[30][2])

for x in range(start, end + 1, delta):
    if not isPrime(x):
        h += 1

print(h)
