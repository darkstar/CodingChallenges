import re

lights = [[0 for y in range(1000)] for x in range(1000)]

def f1(x):
    return x + 1

def f2(x):
    if x > 0:
        return x - 1
    return x

def f3(x):
    return x + 2

with open('input.txt', mode='r') as f:
    lines = [l.rstrip() for l in f.readlines()]

    for line in lines:
        m = re.match('(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)', line)
        [x1, y1, x2, y2] = [int(m.groups()[n]) for n in [1, 2, 3, 4]]
        if m.groups()[0] == 'turn on':
            fun = f1
        elif m.groups()[0] == 'turn off':
            fun = f2
        else:
            fun = f3

        for yy in range(y1, y2+1):
            for xx in range(x1, x2+1):
                lights[xx][yy] = fun(lights[xx][yy])

print(sum([x for col in lights for x in col]))
