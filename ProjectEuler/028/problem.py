
result = 1
for n in range(3, 1002, 2):
    # each layer: n^2
    #             (n^2 - (n-1))
    #             (n^2 - 2(n-1))
    #             (n^2 - 3(n-1))
    result += 4 * (n * n) - 6 * n + 6

print(result)
