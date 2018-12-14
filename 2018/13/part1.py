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

class Cart:
    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.d = d
        self.nextturn = Direction.Left
    def tick(self):
        (nx, ny) = delta[self.d]
        print("x,y =", nx, ny)
        nx += self.x
        ny += self.y
        print("x,y =", nx, ny)
        c = field[nx][ny]
        if c == '/' and self.d in [Direction.Up, Direction.Down]:
            self.d = TurnRight(self.d)
        if c == '/' and self.d in [Direction.Right, Direction.Left]:
            self.d = TurnLeft(self.d)
        if c == '\\' and self.d in [Direction.Up, Direction.Down]:
            self.d = TurnLeft(self.d)
        if c == '\\' and self.d in [Direction.Right, Direction.Left]:
            self.d = TurnRight(self.d)
        if c == '+':
            if self.nextturn == Direction.Left:
                self.d = TurnLeft(self.d)
                self.NextTurn = None
            elif self.nextturn == None:
                self.NextTurn = Direction.Right
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

def check_colission():
    for c in carts:
        for d in [x for x in carts if x != c]:
            if c.x == d.x and c.y == d.y: return True

    return False

with open('input.txt', mode='r') as f:
    lines = f.readlines()
    for y in range(len(lines)):
        for x in range(len(lines[y].rstrip())):
            c = lines[y][x]
            if c == '>' or c == '<':
                field[x][y] = '-'
                carts.append(Cart(x, y, Direction.Left if c == '<' else Direction.Right))
            elif c == '^' or c == 'v':
                field[x][y] = '|'
                carts.append(Cart(x, y, Direction.Up if c == '^' else Direction.Down))
            else:
                field[x][y] = c

tick = 0
while True:
    # sort by x and y position
    carts.sort(key = lambda c: c.y * 150 + c.x)
    do_tick()
    tick += 1
    if check_colission(): break

print('Collision after tick {}'.format(tick))

