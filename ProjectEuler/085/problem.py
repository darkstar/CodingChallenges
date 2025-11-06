# number of rectangles
# an a x b rectangle has (a+1) x (b+1) lines that
# define the bounds of the sub-rectangle
# so the number of ways to choose 2 from (a+1) and (b+1)
# give us the result we need: x * (x + 1) / 2 and y * (y + 1) / 2
def rects(a, b):
    return a * (a + 1) * b * (b + 1) // 4

best = 999999999
result = 0
for x in range(100):
    for y in range(x + 1):
        r = rects(x, y)
        dist = abs(2000000 - r)
        if dist < best:
            best = dist
            result = x * y

print(result)
