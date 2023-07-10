# ref: http://mathworld.wolfram.com/DecimalExpansion.html

def fract(n):
    rest = 1
    for i in range(n):
        rest = (rest * 10) % n
    rest0 = rest
    len = 0
    while True:
        rest = (rest * 10) % n
        len += 1
        if rest == rest0:
            break
    return len

maxfract = 0
maxd = 0

for d in range(1, 1000):
    if fract(d) > maxfract:
        maxfract = fract(d)
        maxd = d

print(maxd)
