import re

class Star:
    def __init__(self, pos, v):
        self.pos = pos
        self.v = v

    def tick(self):
        self.pos = (self.pos[0] + self.v[0], self.pos[1] + self.v[1])

    def untick(self):
        self.pos = (self.pos[0] - self.v[0], self.pos[1] - self.v[1])

class BBox:
    def __init__(self):
        self.xmin = 99999
        self.xmax = -99999
        self.ymin = 99999
        self.ymax = -99999
    def update(self, p):
        if p[0] < self.xmin: self.xmin = p[0]
        if p[0] > self.xmax: self.xmax = p[0]
        if p[1] < self.ymin: self.ymin = p[1]
        if p[1] > self.ymax: self.ymax = p[1]
    def w(self):
        return abs(self.xmax - self.xmin)
    def h(self):
        return abs(self.ymax - self.ymin)
    def size(self):
        return self.w()*self.h()

stars = []
bbox = BBox()

with open('input.txt', mode='r') as f:
    lines = f.readlines()
    for line in lines:
        m = re.match('.*<(.*),(.*)>.*<(.*),(.*)>', line)
        pos = (int(m.groups()[0]), int(m.groups()[1]))
        v = (int(m.groups()[2]), int(m.groups()[3]))
        bbox.update(pos)
        stars.append(Star(pos, v))

while True:
    bbox_new = BBox()
    for star in stars:
        star.tick()
        bbox_new.update(star.pos)

    if bbox_new.size() < bbox.size():
        bbox = bbox_new
    else:
        break

# undo last move
for star in stars:
    star.untick()

l = [[' ' for x in range(bbox.w() + 1)] for y in range(bbox.h() + 1)]

for star in stars:
    l[star.pos[1] - bbox.ymin][star.pos[0] - bbox.xmin] = '*'

for row in l:
    print(''.join(row))

