class Direction:
    Left = 0
    Up = 1
    Right = 2
    Down = 3
    
def TurnLeft(d):
    if d == Direction.Left: return Direction.Down
    if d == Direction.Down: return Direction.Right
    if d == Direction.Right: return Direction.Up
    return Direction.Left

def TurnRight(d):
    if d == Direction.Left: return Direction.Up
    if d == Direction.Down: return Direction.Left
    if d == Direction.Right: return Direction.Down
    return Direction.Right

delta = { Direction.Left: (-1, 0), Direction.Up: (0, -1), Direction.Right: (1, 0), Direction.Down: (0, 1) }

def d2s(d):
    if d == Direction.Left:
        return "Left"
    if d == Direction.Right:
        return "Right"
    if d == Direction.Up:
        return "Up"
    if d == Direction.Down:
        return "Down"
    return "????"

class Cart:
    def __init__(self, x, y, d, name):
        self.x = x
        self.y = y
        self.d = d
        self.nextturn = Direction.Left
        self.name = name
    def __repr__(self):
        return "({},{} @ {})".format(self.x, self.y, d2s(self.d))
    def tick(self):
        (nx, ny) = delta[self.d]
        nx += self.x
        ny += self.y
        c = field[nx][ny]
        if c == '/' and self.d in [Direction.Up, Direction.Down]:
            self.d = TurnRight(self.d)
        elif c == '/' and self.d in [Direction.Right, Direction.Left]:
            self.d = TurnLeft(self.d)
        elif c == '\\' and self.d in [Direction.Up, Direction.Down]:
            self.d = TurnLeft(self.d)
        elif c == '\\' and self.d in [Direction.Right, Direction.Left]:
            self.d = TurnRight(self.d)
        elif c == '+':
            if self.nextturn == Direction.Left:
                self.d = TurnLeft(self.d)
                self.nextturn = ""
            elif self.nextturn == "":
                self.nextturn = Direction.Right
            elif self.nextturn == Direction.Right:
                self.d = TurnRight(self.d)
                self.nextturn = Direction.Left
        self.x = nx
        self.y = ny

field = [[' ' for y in range(150)] for x in range(150)]
carts = []

def do_tick():
    for cart in carts:
        cart.tick()
        coll = check_colission()
        if coll:
            print('Collision after tick {} at ({},{})'.format(tick, coll[0], coll[1]))
            exit(0)

def check_colission():
    for c in carts:
        for d in [x for x in carts if x != c]:
            if c.x == d.x and c.y == d.y: 
                return (c.x, c.y)

    return None

cartnum = 1
with open('input.txt', mode='r') as f:
    lines = f.readlines()
    for y in range(len(lines)):
        for x in range(len(lines[y].rstrip())):
            c = lines[y][x]
            if c == '>' or c == '<':
                field[x][y] = '-'
                carts.append(Cart(x, y, Direction.Left if c == '<' else Direction.Right, str(cartnum)))
                cartnum += 1
            elif c == '^' or c == 'v':
                field[x][y] = '|'
                carts.append(Cart(x, y, Direction.Up if c == '^' else Direction.Down, str(cartnum)))
                cartnum += 1
            else:
                field[x][y] = c

#for y in range(150):
#    row = [field[x][y] for x in range(150)]
#    print("".join(row))

tick = 0
while True:
    # sort by x and y position
    carts.sort(key = lambda c: (c.y, c.x))
    do_tick()
    tick += 1


