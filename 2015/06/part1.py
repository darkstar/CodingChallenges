import re

lights = [[0 for y in range(1000)] for x in range(1000)]

with open('input.txt', mode='r') as f:
    lines = [l.rstrip() for l in f.readlines()]

    for line in lines:
        m = re.match('(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)', line)
        [x1, y1, x2, y2] = [int(m.groups()[n]) for n in [1, 2, 3, 4]]

        for yy in range(y1, y2+1):
            for xx in range(x1, x2+1):
                if m.groups()[0] == 'turn on':
                    lights[xx][yy] = 1
                if m.groups()[0] == 'turn off':
                    lights[xx][yy] = 0
                if m.groups()[0] == 'toggle':
                    lights[xx][yy] = 1 - lights[xx][yy]

print(sum([x for col in lights for x in col]))
