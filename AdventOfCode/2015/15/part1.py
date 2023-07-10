class Ingredient:
    def __init__(self, name, capacity, durability, flavor, texture):
        self.name = name
        self.capacity = capacity
        self.durability = durability
        self.flavor = flavor
        self.texture = texture

ingredients = []
counts = []
best = 0

def evaluate():
    global best

    c = sum([counts[i]*ingredients[i].capacity for i in range(len(counts))])
    d = sum([counts[i]*ingredients[i].durability for i in range(len(counts))])
    f = sum([counts[i]*ingredients[i].flavor for i in range(len(counts))])
    t = sum([counts[i]*ingredients[i].texture for i in range(len(counts))])

    if c < 0: c = 0
    if d < 0: d = 0
    if f < 0: f = 0
    if t < 0: t = 0

    m = c * d * t * f

    if m > best:
        best = m

def iterate(pos, counts):
    if pos == len(ingredients) - 1:
        # final
        counts[pos] = 100 - sum(counts[:-1])
        evaluate()
        return

    # intermediate
    for x in range(len(counts)-pos):
        counts[pos + x] = 0

    for n in range(0, 100 - sum(counts[:(pos + 1)]) + 1):
        counts[pos] = n
        iterate(pos + 1, counts)

with open('input.txt', mode='r') as f:
    lines = f.readlines()
    for l in lines:
        w = l.split()
        name = w[0][:-1]
        c = int(w[2][:-1])
        d = int(w[4][:-1])
        f = int(w[6][:-1])
        t = int(w[8][:-1])
        ingredients.append(Ingredient(name, c, d, f, t))

    counts = [0 for x in range(len(ingredients))]
    iterate(0, counts)

print(best)
