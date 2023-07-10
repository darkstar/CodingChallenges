import itertools

def gen(fn):
    i = 1
    result = []
    while True:
        n = fn(i)
        if n >= 10000:
            return result
        if n >= 1000:
            result.append(n)
        i += 1

def find(numbers, start, end, out):
    if len(numbers) == 1: 
        if start * 100 + end in numbers[0]:
            print(start*100+end + sum(out))
            exit(1)
    for next in numbers:
        for n in next:
            if n // 100 == start:
                find([l for l in numbers if l != next], n % 100, end, out + [n])


funcs = [
        lambda n: (n*(n+1))//2,
        lambda n: n*n,
        lambda n: (n*(3*n-1))//2,
        lambda n: n*(2*n-1),
        lambda n: (n*(5*n-3))//2,
        lambda n: n*(3*n-2)
        ]

def calc_numbers(start, end, proc):
    n = 1
    out = []
    while True:
        z = proc(n)
        if z >= start and z < end: out.append(z)
        if z >= end: return out
        n += 1

# we remove all numbers with a 0 in 3rd position
p = [ list(filter(lambda x: (x//10)%10 != 0, gen(f))) for f in funcs ]

for n in p[5]:
    find(p[:-1], n % 100, n // 100, [n])

