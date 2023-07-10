import functools

@functools.cache
def combs(n, coins = (1, 2, 5, 10, 20, 50, 100, 200)):
    if len(coins) == 0:
        return 0
    c = coins[0]
    coins = coins[1:]
    s = 0
    if n % c == 0:
        s += 1
    for rest in range(0, n, c):
        s += combs(n - rest, coins)
    return s

print(combs(200))

